import matplotlib.pyplot as plt

import trafficLight.evaluation as evaluation


def showTrajectory(params, sims):
    max_acc = params['max_acc']
    min_acc = params['min_acc']
    max_vel = params['max_vel']
    start_pos = params['start_pos']

    logs = [sim.log for sim in sims]

    times = [[s.time for s in log] for log in logs]
    positions = [[s.pos for s in log] for log in logs]
    velocities = [[s.vel for s in log] for log in logs]
    accelerations = [[s.acc for s in log] for log in logs]
    performances = [evaluation.performanceList(sim) for sim in sims]

    maxTime = max(max(t) for t in times)
    deltaAcc = max_acc - min_acc
    minPerformance = evaluation.minPerformance(params)
    maxPerformance = evaluation.maxPerformance()

    plt.subplot(4, 1, 1)

    plt.title("position")
    for p, t in zip(positions, times):
        plt.plot(p, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(start_pos * 1.1, 0.1 * abs(start_pos))
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=start_pos, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 2)

    plt.title("velocity")
    for v, t in zip(velocities, times):
        plt.plot(v, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(-max_vel * 0.1, max_vel * 1.1)
    plt.ylim(0, maxTime)
    plt.axvline(x=0, ymin=0, ymax=1, color='k')
    plt.axvline(x=max_vel, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 3)

    plt.title("acceleration")
    for a, t in zip(accelerations, times):
        plt.plot(a, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(min_acc - 0.1 * deltaAcc, max_acc + 0.1 * deltaAcc)
    plt.ylim(0, maxTime)
    plt.axvline(x=min_acc, ymin=0, ymax=1, color='k')
    plt.axvline(x=max_acc, ymin=0, ymax=1, color='k')

    plt.subplot(4, 1, 4)

    plt.title("perfomance")
    for p, t in zip(performances, times):
        plt.plot(p, t, linewidth=2)
    plt.ylabel("time")
    plt.xlim(minPerformance, maxPerformance)
    plt.ylim(0, maxTime)
    plt.axvline(x=min_acc, ymin=0, ymax=1, color='k')
    plt.axvline(x=max_acc, ymin=0, ymax=1, color='k')

    plt.show()
