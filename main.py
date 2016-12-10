from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from controller import LinearController, PowerLawController, \
    LateBrakeController, CheatController
from visualization import showTrajectory

drivers = [LinearController(), LateBrakeController(),
           PowerLawController(0.5), PowerLawController(3.0),
           CheatController()]
trafficLight = FixedTrafficLight(5)

sims = [TrafficSim(driver, trafficLight, logging=True) for driver in drivers]
for sim in sims:
    sim.run()

showTrajectory([sim.log for sim in sims])
