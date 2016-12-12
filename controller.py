import numpy as np
import tensorflow as tf
import random
from mlp import MLP
from constants import MAX_ACC, MIN_ACC, NUM_OBSERVATION_VARIABLES, START_VEL, \
    START_POS, MAX_VEL


class Controller(object):
    def act(self, pos, vel, time):
        pass


class LinearController(Controller):
    def act(self, pos, vel, time):
        """Brake with a small, constant decceleration to reach
        zero velocity at the traffic light."""
        return 0.5 * START_VEL ** 2 / START_POS


class PowerLawController(Controller):
    def __init__(self, alpha):
        Controller.__init__(self)

        # exponent
        self.alpha = alpha

        # braking time
        self.tb = (alpha + 1) * abs(START_POS) / MAX_VEL

    def act(self, pos, vel, time):
        """Brake such that the velocity follows a power law

            vmax * (1 - t/tb)**alpha

        where tb is the braking time. For alpha=1, this is equal to the
        `LinearController`.
        """
        if time >= self.tb:
            return MIN_ACC  # step on the brake pedal

        a = self.alpha
        tb = self.tb
        return - a * MAX_VEL / tb * (1.0 - time / tb)**(a - 1.0)


class LateBrakeController(Controller):
    def act(self, pos, vel, time):
        """Assumes maximal velocity at the beginning and brakes
        only if it needs to in order to reach stop before the traffic light."""
        brakeDistance = MAX_VEL ** 2 / (2 * abs(MIN_ACC))
        if brakeDistance >= abs(pos):
            return MIN_ACC
        return 0.0


class CheatController(Controller):
    def act(self, pos, vel, time):
        """A perfect but unfair driver that knows the specific time when the
        traffic light switches to green."""
        startTime = 5 - MAX_VEL / MAX_ACC

        if time < startTime:
            brakeAcc = 0.5 * START_VEL**2 / (MAX_VEL**2 / (2.0 * MAX_ACC) + START_POS)
            return brakeAcc
        else:
            return MAX_ACC


class ConstantSpeedController(Controller):
    def __init__(self):
        self.observation = tf.placeholder("float", [None, NUM_OBSERVATION_VARIABLES])
        cost = lambda trainingData, output : tf.reduce_mean(tf.square(trainingData-output))
        # Output: Probabilities to 1. Keep velocity, 2. Accelerate, 3. Decelerate
        self.nn = MLP([NUM_OBSERVATION_VARIABLES, 3], self.observation, [tf.identity], cost)
        self.action = tf.argmax(self.nn.outputLayer, dimension=1)
        self.train()

    def train(self):
        numSteps = 5000
        batchSize = 128
        for i in range(numSteps):
            self.nn.train(self.getTrainingData(batchSize))

    def act(self, pos, vel, time):
        # inp = np.array([pos, vel, time, green])
        inp = np.array([vel])
        inp = inp[np.newaxis,...]
        actionValue = self.nn.session.run(self.action, feed_dict = {
            self.observation : inp
            })[0]
        return [0, MAX_ACC, MIN_ACC][actionValue]

    def getTrainingData(self, size):
        maxVel = 1.0
        velWanted = 0.5
        tolerance = 0.02
        X = np.array([[maxVel * random.random() for i in range(1)] for j in range(size)])
        # Y = np.array([
        #     [1, 0, 0] if abs(vel-velWanted) < tolerance
        #     else [0, 1, 0] if vel < velWanted
        #     else [0, 0, 1]
        #     for (pos, vel, time, green) in X])
        Y = np.array([
            [1, 0, 0] if abs(vel-velWanted) < tolerance
            else [0, 1, 0] if vel < velWanted
            else [0, 0, 1]
            for vel in X])
        return X, Y
