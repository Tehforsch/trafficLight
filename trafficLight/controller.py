class Controller(object):
    def __init__(self):
        # The parameters will be set by the simulation
        super().__init__()

        self.params = {}

    def setup(self):
        """This method is called after the parameters have been set"""
        pass

    def act(self, pos, vel, time):
        raise NotImplementedError()

    def __str__(self):
        return type(self).__name__


class LinearController(Controller):
    def act(self, pos, vel, time):
        """Brake with a small, constant decceleration to reach
        zero velocity at the traffic light."""
        return 0.5 * self.params['start_vel'] ** 2 / self.params['start_pos']


class PowerLawController(Controller):
    def __init__(self, alpha):
        super().__init__()

        # exponent
        self.alpha = alpha

    def setup(self):
        # calculate braking time
        self.tb = (self.alpha + 1) * abs(self.params['start_pos']) / self.params['max_vel']

    def act(self, pos, vel, time):
        """Brake such that the velocity follows a power law

            vmax * (1 - t/tb)**alpha

        where tb is the braking time. For alpha=1, this is equal to the
        `LinearController`.
        """
        if time >= self.tb:
            return self.params['min_acc']  # step on the brake pedal

        a = self.alpha
        tb = self.tb
        return - a * self.params['max_vel'] / tb * (1.0 - time / tb)**(a - 1.0)

    def __str__(self):
        return "PowerLawController alpha = {}".format(self.alpha)


class LateBrakeController(Controller):
    def act(self, pos, vel, time):
        """Assumes maximal velocity at the beginning and brakes
        only if it needs to in order to reach stop before the traffic light."""
        brakeDistance = self.params['max_vel'] ** 2 / (2 * abs(self.params['min_acc']))
        if brakeDistance >= abs(pos):
            return self.params['min_acc']
        return 0.0


class CheatController(Controller):
    def act(self, pos, vel, time):
        """A perfect but unfair driver that knows the specific time when the
        traffic light switches to green."""
        startTime = 5 - self.params['max_vel'] / self.params['max_acc']

        if time < startTime:
            start_vel = self.params['start_vel']
            max_vel = self.params['max_vel']
            max_acc = self.params['max_acc']
            start_pos = self.params['start_pos']
            brakeAcc = 0.5 * start_vel**2 / (max_vel**2 / (2.0 * max_acc) + start_pos)
            return brakeAcc
        else:
            return self.params['max_acc']
