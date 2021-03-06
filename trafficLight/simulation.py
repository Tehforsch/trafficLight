from collections import namedtuple

from trafficLight.constants import DT, NUM_STEPS

DriverState = namedtuple('DriveState', ['time', 'pos', 'vel', 'acc'])


class Simulation(object):
    """
    Handles a simulation of
    1. A car at position pos moving towards a traffic-light at speed vel.
    2. A traffic light at position 0 that will be red initially and turn green
       at some point in time.
    3. A driver who is given the position and velocity of the car as well as
       the state of the traffic light and decides on the acceleration of the
       car.
    """

    def __init__(self, params, driver, logging=False):
        self.driver = driver
        self.driver.params = params
        self.driver.setup()

        self.params = params

        self.pos = params['start_pos']
        self.vel = params['start_vel']

        self.max_acc = params['max_acc']
        self.min_acc = params['min_acc']

        self.time = 0
        self.numSteps = 0
        self.logging = logging

        if self.logging:
            self.log = []

    def truncate(self, acc):
        """Ensure that the acceleration is in the interval [MIN_ACC, MAX_ACC]."""
        acc = max(min(acc, self.max_acc), self.min_acc)
        return acc

    def integrate(self, acc):
        """Update the state by integrating over a short time interval."""
        self.vel += acc * DT
        if self.vel < 0:
            self.vel = 0.0
        self.pos += self.vel * DT

    def timestep(self):
        """Perform a single simulation step."""
        self.numSteps += 1
        self.time += DT

        acc = self.driver.act(self.pos, self.vel, self.time)
        acc = self.truncate(acc)
        self.integrate(acc)

        if self.logging:
            state = DriverState(self.time, self.pos, self.vel, acc)
            self.log.append(state)

    def run(self):
        """Run the simulation until the traffic light turns green"""
        while self.numSteps < NUM_STEPS:
            self.timestep()
