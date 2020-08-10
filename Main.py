# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:50:20 2020

@author: Daniel
"""

import sys
from Cell_State import CellState
from colors import *

import pygame

from Game_Of_Life_Simulation import *
from Rule import *

# from enum import Enum
from Simulation_States import *


# START PYGAME ------------------------------------------------------------------------------------------------------------------ #

# Initialize Screen

pygame.init()           # INITIALIZE ENGINE

SCREEN_BASE_SIZE = (860,860)
SCREEN_TITLE = "Game_Of_Life"
SCREEN_SIZE_MULTIPLIER = (1,1)
SCREEN_COMPUTED_SIZE = (int(SCREEN_BASE_SIZE[0] * SCREEN_SIZE_MULTIPLIER[0]) ,int(SCREEN_BASE_SIZE[1] * SCREEN_SIZE_MULTIPLIER[1]))
clock = pygame.time.Clock()
TICK_RATE = 1000
is_simulation_over = False

# create the new window
screen = pygame.display.set_mode(( SCREEN_COMPUTED_SIZE[0] ,SCREEN_COMPUTED_SIZE[1]))     # INITIALIZE WINDOW
screen.fill((255, 255, 255))
pygame.display.set_caption(SCREEN_TITLE)

# EXECUTION --------------------------------------------------------------------------------------------------------------------- #
    
ROW_AMOUNT = 48
COLL_AMOUNT = 48

# CREATE THE RULES -------------------------------------------------------------------------------------------------------------- #

simulation_rules = []
simulation_rules.append(Rule("Death by underpopulation",CellState.FILLED,CellState.FILLED,0,1,CellState.EMTPY))
simulation_rules.append(Rule("sustainable life",CellState.FILLED,CellState.FILLED,2,3,CellState.FILLED))
simulation_rules.append(Rule("Death by overpopulation",CellState.FILLED,CellState.FILLED,4,8,CellState.EMTPY))     # -1 == infinito a la hora de comprobarlo
simulation_rules.append(Rule("Birth",CellState.EMTPY,CellState.FILLED,3,3,CellState.FILLED))

game_of_life_ruleset = Ruleset(simulation_rules)

sys.stdout.write(YELLOW + BOLD)     # set the color of the text
print ("\t Ruleset configured succesfully")
sys.stdout.write(RESET)             # RESET the color of the text


# CREATE SIMULATION ------------------------------------------------------------------------------------------------------------- #
sys.stdout.write(BLUE)
game_of_life = GameOfLifeSimulation(COLL_AMOUNT, ROW_AMOUNT,SCREEN_COMPUTED_SIZE[0],SCREEN_COMPUTED_SIZE[1],game_of_life_ruleset)

sys.stdout.write(YELLOW + BOLD)     # set the color of the text
print ("\t Setup performed succesfully")
sys.stdout.write(RESET)             # RESET the color of the text


# # MAIN SYSTEM LOOP -------------------------------------------------------------------------------------------------------------
current_simulation_state = SimulationStates.COMPUTING
while is_simulation_over == False:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        is_simulation_over = True
    
    pygame.display.update()
    clock.tick(TICK_RATE)
    
    # tick rate testing (background)
    # screen.fill(get_random_color(False))

    # ACT DEPENDING THE SIMULATION STATE
    if current_simulation_state == SimulationStates.COMPUTING:
        # game_of_life.compute_cells()
        #current_simulation_state = SimulationStates.UPDATING

        # if the return of the function is not none is because it just completed all the cells
        if game_of_life.compute_cell_per_cell() != None:
            current_simulation_state = SimulationStates.UPDATING


    elif current_simulation_state == SimulationStates.UPDATING:
        # game_of_life.update_cells()
        # current_simulation_state = SimulationStates.COMPUTING
        
        if game_of_life.update_cell_per_cell() != None:
            current_simulation_state = SimulationStates.COMPUTING


    # debug cells data
    # game_of_life.cell_matrix.print_cells_data()

    # redraw the matrix
    game_of_life.draw_cells(screen)

print ("Exiting window")
pygame.quit()
