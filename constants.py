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
DT = 0.1
NUM_STEPS = int(MAX_TIME / DT)

# NN parameters
NUM_OBSERVATION_VARIABLES = 1
STDDEV = 0.01  # Standard deviation of initial weight distribution
LEARNING_PARAMETER = 0.01
