from constants import MAX_VEL, MAX_ACC, START_POS, DT, RUNNING_RED_LIGHT_PUNISHMENT

def totalPerformance(sim, trafficLight):
    return trafficLight.score(performance(sim.log))

def performance(log):
    epsilon = DT * MAX_VEL
    if log[-1].pos > epsilon:
        return RUNNING_RED_LIGHT_PUNISHMENT
    return [s.pos - 0.5 * (MAX_VEL - s.vel)**2 / MAX_ACC for s in log]

def minPerformance():
    return START_POS - 0.5 * MAX_VEL**2 / MAX_ACC

def maxPerformance():
    return 0
