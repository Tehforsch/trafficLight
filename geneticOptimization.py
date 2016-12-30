from trafficLight.constants import MAX_TIME
from trafficLight.trafficLight import UniformTrafficLight
import trafficLight.geneticOptimization as geneticOpt

params = {
    'max_acc': 1.0,
    'min_acc': -2.0,
    'max_vel': 1.0,
    'start_vel': 1.0,
    'start_pos': -1.0
}

trafficLight = UniformTrafficLight(MAX_TIME)
geneticOpt.optimize(params, trafficLight)
