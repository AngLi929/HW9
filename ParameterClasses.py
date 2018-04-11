from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):

    Well = 0
    Stroke = 1
    PostStroke = 2
    Dead = 3


class Therapies(Enum):

    NoTherapy = 0
    Anti = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.Well

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        if self._therapy == Therapies.NoTherapy:
            self._prob_matrix = Data.TRANS_MATRIX
        else:
            self._prob_matrix = Data.TRANS_MATRIX_ANTI

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]
