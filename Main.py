# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:50:20 2020

@author: Daniel
"""
import sys
from colors import *

import pygame

from Game_Of_Life_Simulation import *
from Rule import *

# EXECUTION
    
ROW_AMOUNT = 10
COLL_AMOUNT = 10
AMOUNT_OF_INSTANCES = ROW_AMOUNT * COLL_AMOUNT

# CREATE THE RULES
simulation_rules = []
rule = Rule("New Rule",1,0,1,5,1)


# create simulation
sys.stdout.write(BLUE)
game_of_life = GameOfLifeSimulation(COLL_AMOUNT, ROW_AMOUNT)

sys.stdout.write(GREEN)   # set the color of the text
print ("Setup performed succesfully")
sys.stdout.write(RESET)   # set the color of the text
