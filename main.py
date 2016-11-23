from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from controller import ConstantSpeedController, StupidController

driver = ConstantSpeedController()
driver.train()
s = TrafficSim(driver, FixedTrafficLight(5))
s.run()

