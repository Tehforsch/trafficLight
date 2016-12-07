from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from controller import ConstantSpeedController, LinearController, LateBrakeController
from visualization import showTrajectory

# driver = ConstantSpeedController()
# driver.train()
# driver = LinearController()
driver = LateBrakeController()
s = TrafficSim(driver, FixedTrafficLight(5), logging=True)
s.run()
showTrajectory(s.log)
