# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:08:07 2020

@author: Daniel
"""

from enum import Enum

# STATES OF THE SIMULATION
class SimulationStates(Enum):
    IDLE = -1
    COMPUTING = 0
    UPDATING = 1