from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from controller import LinearController, LateBrakeController, CheatController
from visualization import showTrajectory

driver1 = LinearController()
s1 = TrafficSim(driver1, FixedTrafficLight(5), logging=True)
s1.run()

driver2 = LateBrakeController()
s2 = TrafficSim(driver2, FixedTrafficLight(5), logging=True)
s2.run()

driver3 = CheatController()
s3 = TrafficSim(driver3, FixedTrafficLight(5), logging=True)
s3.run()

showTrajectory([s1.log, s2.log, s3.log])
