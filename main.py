from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from controller import LinearController, LateBrakeController, CheatController
from visualization import showTrajectory

drivers = [LinearController(), LateBrakeController(), CheatController()]
trafficLight = FixedTrafficLight(5)

sims = [TrafficSim(driver, trafficLight, logging=True) for driver in drivers]
for sim in sims:
    sim.run()

showTrajectory([sim.log for sim in sims])
