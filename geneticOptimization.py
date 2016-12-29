from trafficLight.constants import MAX_TIME
from trafficLight.trafficLight import UniformTrafficLight
import trafficLight.geneticOptimization as geneticOpt

trafficLight = UniformTrafficLight(MAX_TIME)
geneticOpt.optimize(trafficLight)
