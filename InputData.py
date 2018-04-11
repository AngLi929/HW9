# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)

ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15,    0,    0.1],
    [0,     0,    1,    0],
    [0,     0.25,      0.55,   0.2],
    [0,     0,         0,      1],
    ]

TRANS_MATRIX_ANTI = [
    [0.75,  0.15,    0,    0.1],
    [0,     0,    1,    0],
    [0,     0.1625,      0.701,   0.1365],
    [0,     0,         0,      1],
    ]
