from constants import MAX_VEL, MAX_ACC, START_POS, DT, RUNNING_RED_LIGHT_PUNISHMENT

def totalPerformance(sim, trafficLight):
    return trafficLight.score(performance(sim.log))

def performance(log):
    return [localPerformance(state) for state in log]

def localPerformance(state):
    epsilon = DT * MAX_VEL
    if state.pos > epsilon:
        return RUNNING_RED_LIGHT_PUNISHMENT
    else:
        return state.pos - 0.5 * (MAX_VEL - state.vel)**2 / MAX_ACC

def minPerformance():
    return START_POS - 0.5 * MAX_VEL**2 / MAX_ACC

def maxPerformance():
    return 0
