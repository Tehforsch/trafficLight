import matplotlib.pyplot as plt

from constants import POS_START, MIN_ACC, MAX_ACC, MAX_ALLOWED_VEL


def showTrajectory(states):
    times = list(s.time for s in states)
    positions = list(s.pos for s in states)
    velocities = list(s.vel for s in states)
    accelerations = list(s.acc for s in states)

    maxTime = max(times)
    deltaAcc = MAX_ACC - MIN_ACC

    plt.subplot(3, 1, 1)

    plt.title("position")
    plt.plot(positions, times, linewidth=2)
    plt.ylabel("time")
    plt.xlim(POS_START * 1.1, 0.1 * abs(POS_START))
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=POS_START, ymin=0, ymax=1, color='k')

    plt.subplot(3, 1, 2)

    plt.title("velocity")
    plt.plot(velocities, times, linewidth=2)
    plt.ylabel("time")
    plt.xlim(-MAX_ALLOWED_VEL * 0.1, MAX_ALLOWED_VEL * 1.1)
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_ALLOWED_VEL, ymin=0, ymax=1, color='k')

    plt.subplot(3, 1, 3)

    plt.title("acceleration")
    plt.plot(accelerations, times, linewidth=2)
    plt.ylabel("time")
    plt.xlim(MIN_ACC - 0.1 * deltaAcc, MAX_ACC + 0.1 * deltaAcc)
    plt.ylim(0, maxTime)
    plt.axvline(x=MIN_ACC, ymin=0, ymax=1, color='k')
    plt.axvline(x=MAX_ACC, ymin=0, ymax=1, color='k')

    plt.show()
