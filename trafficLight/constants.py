# Traffic light parameters
MAX_TIME = 5

# Simulation parameters
DT = 0.00005
NUM_STEPS = int(MAX_TIME / DT)

# Evaluation parameters
RUNNING_RED_LIGHT_EPSILON = 1e-4
RUNNING_RED_LIGHT_PUNISHMENT = -100
