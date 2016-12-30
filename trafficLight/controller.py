from trafficLight.constants import MAX_ACC, MIN_ACC, START_VEL, START_POS, MAX_VEL


class Controller(object):
    def act(self, pos, vel, time):
        pass

    def __str__(self):
        return type(self).__name__


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

    def __str__(self):
        return "PowerLawController alpha = {}".format(self.alpha)


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
