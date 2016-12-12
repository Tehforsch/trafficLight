from constants import START_POS, START_VEL, MAX_ACC, MIN_ACC, DT
from collections import namedtuple

DriverState = namedtuple('DriveState', ['time', 'pos', 'vel', 'acc'])


class TrafficSim(object):
    """
    Handles a simulation of
    1. A car at position pos moving towards a traffic-light at speed vel.
    2. A traffic light at position 0 that will be red initially and turn green
       at some point in time.
    3. A driver who is given the position and velocity of the car as well as
       the state of the traffic light and decides on the acceleration of the
       car.
    """

    def __init__(self, driver, maxTime, logging=False):
        self.driver = driver
        self.maxTime = maxTime
        self.pos = START_POS
        self.vel = START_VEL
        self.time = 0
        self.numSteps = 0
        self.logging = logging

        if self.logging:
            self.log = []

    def truncate(self, acc):
        """Ensure that the acceleration is in the interval [MIN_ACC, MAX_ACC]."""
        acc = max(min(acc, MAX_ACC), MIN_ACC)
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

        # if self.numSteps % 100 == 0:
            # print("{:.2} {:.2} {:.2}".format(self.pos, self.vel, acc))

        if self.logging:
            self.log.append(DriverState(time=self.time, pos=self.pos,
                                        vel=self.vel, acc=acc))

    def run(self):
        """Run the simulation until the traffic light turns green"""
        while self.time < self.maxTime:
            self.timestep()
