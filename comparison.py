from trafficLight.simulation import Simulation
from trafficLight.trafficLight import UniformTrafficLight
from trafficLight.controller import LinearController, PowerLawController, \
    LateBrakeController, CheatController
from trafficLight.visualization import showTrajectory
from trafficLight.evaluation import totalPerformance
from trafficLight.constants import MAX_TIME

trafficLight = UniformTrafficLight(MAX_TIME)

drivers = [LinearController(),
           LateBrakeController(),
           PowerLawController(0.5),
           PowerLawController(3.0),
           CheatController()]
sims = [Simulation(driver, logging=True) for driver in drivers]
for sim in sims:
    sim.run()

print("Scores:")
for sim in sims:
    perf = totalPerformance(sim, trafficLight)
    print("{name:<35}: {perf:0.4f}".format(name=str(sim.driver), perf=perf))

showTrajectory([sim.log for sim in sims])
