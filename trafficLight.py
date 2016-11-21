class FixedTrafficLight(object):
    def __init__(self, greenTime):
        self.greenTime = greenTime

    def isGreen(self, time):
        return time >= self.greenTime
