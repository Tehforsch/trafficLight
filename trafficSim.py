from constants import POS_START, VEL_START, MAX_ACC, MIN_ACC, DT, MAX_TIME, MAX_ALLOWED_VEL

class TrafficSim(object):
    """Handles a simulation of 
    1. A car at position pos moving towards (hopefully) a traffic-light
    at speed vel.
    2. A traffic light at position 0 that will be red initially and turn green
    at some point in time.
    3. A driver who is given the position and velocity of the car as well as the
    state of the traffic light and decides on the acceleration of the car"""
    def __init__(self, driver, trafficLight):
        self.driver = driver
        self.trafficLight = trafficLight
        self.pos = POS_START
        self.vel = VEL_START
        self.time = 0

    def truncate(self, acc):
        return max(min(acc, MAX_ACC), MIN_ACC)

    def integrate(self, acc):
        self.vel += acc * DT
        self.pos += self.vel * DT

    def timestep(self):
        self.time += DT
        acc = self.driver.act(self.pos, self.vel, self.trafficLight.isGreen(self.time))
        acc = self.truncate(acc)
        self.integrate(acc)

    def run(self):
        """Run the simulation until either
        1. The car has reached the maximum allowed velocity
        somewhere behind the traffic light
        2. The simulation has run for too long.
        """
        while True:
            self.timestep()
            if self.time > MAX_TIME:
                break
            if self.pos > 0 and self.vel >= MAX_ALLOWED_VEL:
                break
