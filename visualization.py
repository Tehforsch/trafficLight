import matplotlib.pyplot as plt


def showTrajectory(states):
    times = list(s.time for s in states)
    positions = list(s.pos for s in states)

    plt.title("Traffic light simulation")
    plt.plot(positions, times)
    plt.xlabel("position")
    plt.ylabel("time")
    plt.axvline(x=0, ymin=0, ymax=1)
    plt.show()
