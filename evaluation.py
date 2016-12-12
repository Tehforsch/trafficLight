from constants import MAX_ALLOWED_VEL, MAX_ACC, POS_START

def totalPerformance(sim, trafficLight):
    return trafficLight.score(performance(sim.log))

def performance(log):
    return [s.pos - 0.5 * (MAX_ALLOWED_VEL - s.vel)**2 / MAX_ACC for s in log]

def minPerformance():
    return POS_START - 0.5 * MAX_ALLOWED_VEL**2 / MAX_ACC

def maxPerformance():
    return 0
