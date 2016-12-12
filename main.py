from trafficSim import TrafficSim
from trafficLight import TrafficLight, UniformTrafficLight
from controller import LinearController, PowerLawController, \
    LateBrakeController, CheatController
from visualization import showTrajectory
import evaluation

drivers = [LinearController(), 
           LateBrakeController(),
           PowerLawController(0.5), 
           PowerLawController(3.0), 
           CheatController()]
trafficLight = UniformTrafficLight(5)

sims = [TrafficSim(driver, trafficLight.maxTime, logging=True) for driver in drivers]
for sim in sims:
    sim.run()

def printTotalScores(sims):
    print("Total scores:")
    for sim in sims:
        name = str(sim.driver)
        total = evaluation.totalPerformance(sim, trafficLight)
        print("{}: {}".format(name, total))

printTotalScores(sims)
showTrajectory([sim.log for sim in sims])
