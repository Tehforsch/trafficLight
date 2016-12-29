import numpy as np

from .constants import DT


class TrafficLight(object):
    def __init__(self, maxTime):
        self.maxTime = maxTime

    def score(self, performances):
        return performances[-1]


class ProbabilityDistributionTrafficLight(TrafficLight):
    """
    Represents a traffic light for which the time is not
    known in advance and is instead represented by a probability
    distribution of turning green as a function of time.
    """
    def __init__(self, distribution):
        self.distribution = distribution
        maxTime = len(self.distribution) * DT
        super().__init__(maxTime)

    def score(self, performances):
        return self.distribution.expectedValue(performances)


class UniformTrafficLight(ProbabilityDistributionTrafficLight):
    """
    Represents a traffic light with a uniform probability
    distribution with a cutoff after some time.
    """
    def __init__(self, maxTime):
        super().__init__(UniformDistribution(maxTime, DT))


def isclose(x1, x2):
    epsilon = 1e-10
    return abs(x1 - x2) < epsilon


class Distribution(object):
    def __init__(self, density):
        """
        Represents a probability distribution by its
        probability density.
        """
        self.density = density
        assert isclose(np.sum(self.density), 1), "The total probability is not 1."

    def expectedValue(self, values):
        return np.sum(np.multiply(self.density, values))

    def __len__(self):
        return len(self.density)


class UniformDistribution(Distribution):
    """
    Represents a uniform distribution with a cutoff at some maximum value, i.e.
    p(t) =  { 1/T if t <= T
            { 0   else
    Values are discretized with stepSize resulting in a total of
    T / stepSize values.
    """
    def __init__(self, T, stepSize):
        numSteps = int(T / stepSize)
        probabilityPerStep = 1 / numSteps
        probabilityDensity = np.full((numSteps,), probabilityPerStep)
        super().__init__(probabilityDensity)

    def __str__(self):
        return str(self.density)
