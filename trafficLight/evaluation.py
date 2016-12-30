from trafficLight.constants import RUNNING_RED_LIGHT_PUNISHMENT, RUNNING_RED_LIGHT_EPSILON


def score(sim, trafficLight):
    pos_latest = sim.log[-1].pos
    if pos_latest > RUNNING_RED_LIGHT_EPSILON:
        return RUNNING_RED_LIGHT_PUNISHMENT
    else:
        return trafficLight.score(performanceList(sim))


def performanceList(sim):
    max_vel = sim.params['max_vel']
    max_acc = sim.params['max_acc']
    return [performance(state, max_vel, max_acc) for state in sim.log]


def performance(state, max_vel, max_acc):
    return state.pos - 0.5 * (max_vel - state.vel)**2 / max_acc


def minPerformance(params):
    return params['start_pos'] - 0.5 * params['max_vel']**2 / params['max_acc']


def maxPerformance():
    return 0.0
