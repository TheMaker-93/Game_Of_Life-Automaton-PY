# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:42:42 2020

@author: Daniel
"""

from enum import Enum

class CellSimulationStages(Enum):
    IDLE = 0
    COMPUTING = -1
    UPDATING = 1