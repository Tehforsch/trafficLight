from trafficSim import TrafficSim
from trafficLight import FixedTrafficLight
from driver import StupidDriver

s = TrafficSim(StupidDriver(), FixedTrafficLight(5))
s.run()
