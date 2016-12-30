import matplotlib.pyplot as plt

from trafficLight.constants import START_POS, MIN_ACC, MAX_ACC, MAX_VEL
import trafficLight.evaluation as evaluation


def showTrajectory(logs):
    times = [[s.time for s in log] for log in logs]
    positions = [[s.pos for s in log] for log in logs]
    velocities = [[s.vel for s in log] for log in logs]
    accelerations = [[s.acc for s in log] for log in logs]
    performances = [evaluation.performance(log) for log in logs]

    maxTime = max(max(t) for t in times)
    deltaAcc = MAX_ACC - MIN_ACC
    minPerformance = evaluation.MIN_PERFORMANCE
    maxPerformance = evaluation.MAX_PERFORMANCE

    plt.subplot(4, 1, 1)

    plt.title("position")
    for p, t in zip(positions, times):
        plt.plot(p, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(START_POS * 1.1, 0.1 * abs(START_POS))
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=START_POS, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 2)

    plt.title("velocity")
    for v, t in zip(velocities, times):
        plt.plot(v, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(-MAX_VEL * 0.1, MAX_VEL * 1.1)
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_VEL, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 3)

    plt.title("acceleration")
    for a, t in zip(accelerations, times):
        plt.plot(a, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(MIN_ACC - 0.1 * deltaAcc, MAX_ACC + 0.1 * deltaAcc)
    plt.ylim(0, maxTime)
    plt.axvline(x=MIN_ACC, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_ACC, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 4)

    plt.title("perfomance")
    for p, t in zip(performances, times):
        plt.plot(p, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(minPerformance, maxPerformance)
    plt.ylim(0, maxTime)
    plt.axvline(x=MIN_ACC, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_ACC, ymin=0, ymax=1, color='k')

    plt.show()
