# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:20:17 2020

@author: Daniel
"""

import sys
from colors import *


class Rule:
    
    _name = "not_named"
    
    _selected_cell_state = 0
    
    _selected_cell_neighbor_state = 0
    _neighbor_min_amount = -1
    _neighbor_max_amount = -1
    
    _selected_cell_end_state = 0
    
    def __init__(self,name ,targeted_cell_state,neighbor_cell_state, neighbor_min_amount,neighbor_max_amount, targeted_cell_end_state):
        
        self._name = name
        
        self._selected_cell_state = targeted_cell_state
        
        self._selected_cell_neighbor_state = neighbor_cell_state
        self._neighbor_min_amount = neighbor_max_amount
        self._neighbor_max_amount = neighbor_max_amount
        
        self._selected_cell_end_state = targeted_cell_end_state
        
        sys.stdout.write(GREEN)
        print ("Rule " + str(self._name) + "has been succesfully created and added to the simulation" )
