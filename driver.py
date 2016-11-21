from constants import MAX_ACC

class StupidDriver(object):
    def act(self, pos, vel, green):
        if not green:
            return 0
        return MAX_ACC # always accelerate
