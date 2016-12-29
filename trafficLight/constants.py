# Physical constants
MAX_ACC = 1.0
MIN_ACC = -2.0
MAX_VEL = 1.0

# Initial parameters
START_POS = -1.0
START_VEL = MAX_VEL

# Traffic light parameters
MAX_TIME = 5

# Simulation parameters
DT = 0.00005
NUM_STEPS = int(MAX_TIME / DT)

# Learning/performance parameters
RUNNING_RED_LIGHT_EPSILON = 1e-4
RUNNING_RED_LIGHT_PUNISHMENT = -100
