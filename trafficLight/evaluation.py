from .constants import MAX_VEL, MAX_ACC, START_POS, \
    RUNNING_RED_LIGHT_PUNISHMENT, RUNNING_RED_LIGHT_EPSILON


def totalPerformance(sim, trafficLight):
    return trafficLight.score(performance(sim.log))


def performance(log):
    return [localPerformance(state) for state in log]


def localPerformance(state):
    if state.pos > RUNNING_RED_LIGHT_EPSILON:
        return RUNNING_RED_LIGHT_PUNISHMENT
    else:
        return state.pos - 0.5 * (MAX_VEL - state.vel)**2 / MAX_ACC


MIN_PERFORMANCE = START_POS - 0.5 * MAX_VEL**2 / MAX_ACC
MAX_PERFORMANCE = 0.0
