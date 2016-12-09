import matplotlib.pyplot as plt

from constants import POS_START, MIN_ACC, MAX_ACC, MAX_ALLOWED_VEL


def showTrajectory(logs):
    times = [[s.time for s in log] for log in logs]
    positions = [[s.pos for s in log] for log in logs]
    velocities = [[s.vel for s in log] for log in logs]
    accelerations = [[s.acc for s in log] for log in logs]
    performances = [[s.pos - 0.5 * (MAX_ALLOWED_VEL - s.vel)**2 / MAX_ACC for s in log] for log in logs]

    maxTime = max(max(t) for t in times)
    deltaAcc = MAX_ACC - MIN_ACC
    minPerformance = POS_START - 0.5 * MAX_ALLOWED_VEL**2 / MAX_ACC
    maxPerformance = 0

    plt.subplot(4, 1, 1)

    plt.title("position")
    for p, t in zip(positions, times):
        plt.plot(p, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(POS_START * 1.1, 0.1 * abs(POS_START))
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=POS_START, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 2)

    plt.title("velocity")
    for v, t in zip(velocities, times):
        plt.plot(v, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(-MAX_ALLOWED_VEL * 0.1, MAX_ALLOWED_VEL * 1.1)
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_ALLOWED_VEL, ymin=0, ymax=1, color='k')

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
