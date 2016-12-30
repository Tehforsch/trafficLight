import random

import numpy as np

from trafficLight.visualization import showTrajectory
from trafficLight.evaluation import totalPerformance
from trafficLight.simulation import Simulation
import trafficLight.constants as constants


class GeneticOptimization(object):
    """
    Contains methods for the optimization of a given fitness function.
    The algorithm works as follows
    1. Randomly create individuals with different properties (parameters)
    2. Selectively cull the population such that only fit individuals survive
    3. Create a new generation of individuals by mutation (randomly adjusting parameters)
    and by crossover between different individuals (mixing of parameters)
    Step 2. and 3. are then iterated a number of generations until (hopefully)
    a "steady-state" is reached.

    This algorithm works for a generalized class of individuals
    which can be generated by a factory method and provide
    the methods
    1. mutate
    2. crossbreed
    3. fitness
    """
    def __init__(self, individualFactory):
        self.individualFactory = individualFactory
        # Constants
        self.numIndividuals = 100
        self.numAfterCulling = 50
        self.proportionGeneratedThroughMutation = 0.5
        self.mutationParameter = 1.0
        self.mutationDecay = 0.001  # How much the mutation parameter decreases with every timestep
        self.numIterations = 1000
        self.numGeneration = 0
        self.generation = [self.individualFactory() for n in range(self.numIndividuals)]
        # Visualization
        self.numToPlot = 10
        self.printInterval = 10
        self.plotInterval = 100

    def iterate(self):
        self.generation.sort(key=lambda x : x.fitness, reverse=True)
        self.generation = self.generation[:self.numAfterCulling]
        self.outputInfo()
        numToReplenish = self.numIndividuals - self.numAfterCulling
        newIndividuals = [self.getNewIndividual() for i in range(numToReplenish)]
        self.generation = self.generation + newIndividuals
        assert len(self.generation) == self.numIndividuals
        self.mutationParameter *= 1 - self.mutationDecay

    def getNewIndividual(self):
        if random.random() < self.proportionGeneratedThroughMutation:
            randomIndividual = random.choice(self.generation)
            return randomIndividual.mutate(self.mutationParameter)
        else:
            randomIndividuals = random.sample(self.generation, 2)
            return randomIndividuals[0].crossbreed(randomIndividuals[1])

    def optimize(self):
        for self.numGeneration in range(self.numIterations):
            self.iterate()

    def outputInfo(self):
        if self.numGeneration % self.printInterval == 0:
            print("Fittest individual: {}".format(max(self.generation, key=lambda individual: individual.fitness)))
        if self.numGeneration % self.plotInterval == 0:
            showTrajectory([individual.sim.log for individual in self.generation[:self.numToPlot]])


class StrategyDriver(object):
    def __init__(self, acceleration):
        self.acceleration = iter(acceleration)

    def act(self, pos, vel, time):
        return next(self.acceleration)


class Strategy(object):
    """
    Contains a generic strategy for approaching a traffic-light
    which is given by a discretized function a(t)
    """
    def __init__(self, acceleration, trafficLight):
        self.acceleration = acceleration
        self.trafficLight = trafficLight
        # Determine fitness by running the simulation
        driver = StrategyDriver(self.acceleration)
        self.sim = Simulation(driver, logging=True)
        self.sim.run()
        self.fitness = totalPerformance(self.sim, self.trafficLight)

    def mutate(self, mutationParameter):
        """Create a new strategy by changing each value with probability
        mutationParameter. The changes are uniformly distributed between
        -maxChange and maxChange.
        (mutationParameter = 1 -> All values are changed
         mutationParameter = 0 -> No values are changed)
        Afterwards, truncate each value to physically
        plausible values (between MIN_ACC and MAX_ACC)"""
        maxChange = 0.1
        doChange = np.random.binomial(n=1, p=mutationParameter, size=len(self.acceleration))
        changeAmount = np.random.uniform(low=-maxChange, high=maxChange, size=len(self.acceleration))
        effectiveChange = doChange * changeAmount
        newValues = self.acceleration + effectiveChange
        truncated = np.clip(newValues, a_min=constants.MIN_ACC, a_max=constants.MAX_ACC)
        return Strategy(truncated, self.trafficLight)

    def crossbreed(self, individual):
        acceleration = 0.5 * (individual.acceleration + self.acceleration)
        return Strategy(acceleration, self.trafficLight)

    def __str__(self):
        return str(self.fitness)


def optimize(trafficLight):
    def strategyFactory():
        acceleration = np.random.uniform(
            low=constants.MIN_ACC,
            high=constants.MAX_ACC,
            size=constants.NUM_STEPS
        )
        return Strategy(acceleration, trafficLight)
    opt = GeneticOptimization(strategyFactory)
    opt.optimize()
