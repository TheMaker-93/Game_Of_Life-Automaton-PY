# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:50:20 2020

@author: Daniel
"""

import sys
from Cell_State import CellState
from colors import ConsoleColor
from colors import get_random_color

import pygame

from Game_Of_Life_Simulation import GameOfLifeSimulation
from Rule import Rule
from Rule import Ruleset
from random import seed

# from enum import Enum
from Simulation_States import SimulationStates
from Cellular_Automaton_Execution_Stage import CellularAutomatonExecutionStage


# START PYGAME ------------------------------------------------------------------------------------------------------------------ #

# Initialize Screen

pygame.init()           # INITIALIZE ENGINE

SCREEN_BASE_SIZE = (920,920)
SCREEN_TITLE = "Game_Of_Life"
SCREEN_SIZE_MULTIPLIER = (1,1)
SCREEN_COMPUTED_SIZE = (int(SCREEN_BASE_SIZE[0] * SCREEN_SIZE_MULTIPLIER[0]) ,int(SCREEN_BASE_SIZE[1] * SCREEN_SIZE_MULTIPLIER[1]))
clock = pygame.time.Clock()
TICK_RATE = 60
is_simulation_over = False

# create the new window
screen = pygame.display.set_mode(( SCREEN_COMPUTED_SIZE[0] ,SCREEN_COMPUTED_SIZE[1]))     # INITIALIZE WINDOW
screen.fill((255, 255, 255))
pygame.display.set_caption(SCREEN_TITLE)

# EXECUTION --------------------------------------------------------------------------------------------------------------------- #
    
ROW_AMOUNT = 30
COLL_AMOUNT = 30
MATRIX_INITIALIZATION_SEED = 0

# CREATE THE RULES -------------------------------------------------------------------------------------------------------------- #

# Here we create the rules that the system will be using
simulation_rules = []
simulation_rules.append(Rule("Death by underpopulation",CellState.FILLED,CellState.FILLED,0,1,CellState.EMPTY))
simulation_rules.append(Rule("sustainable life",CellState.FILLED,CellState.FILLED,2,3,CellState.FILLED))
simulation_rules.append(Rule("Death by overpopulation",CellState.FILLED,CellState.FILLED,4,8,CellState.EMPTY))     # -1 == infinito a la hora de comprobarlo
simulation_rules.append(Rule("Birth",CellState.EMPTY,CellState.FILLED,3,3,CellState.FILLED))

# and pack them into the ruleset object
game_of_life_ruleset = Ruleset(simulation_rules)

sys.stdout.write(ConsoleColor.YELLOW + ConsoleColor.BOLD)     # set the color of the text
print ("\t Ruleset configured succesfully")
sys.stdout.write(ConsoleColor.RESET)             # RESET the color of the text


# CREATE SIMULATION ------------------------------------------------------------------------------------------------------------- #
sys.stdout.write(ConsoleColor.BLUE)
seed(MATRIX_INITIALIZATION_SEED)                  # set the seed for the random initialization
game_of_life = GameOfLifeSimulation(COLL_AMOUNT, ROW_AMOUNT,SCREEN_COMPUTED_SIZE[0],SCREEN_COMPUTED_SIZE[1],game_of_life_ruleset)

sys.stdout.write(ConsoleColor.YELLOW + ConsoleColor.BOLD)     # set the color of the text
print ("\t Setup performed succesfully")
sys.stdout.write(ConsoleColor.RESET)             # RESET the color of the text


# # MAIN SYSTEM LOOP -------------------------------------------------------------------------------------------------------------
current_interaction_state = CellularAutomatonExecutionStage.EDIT_MODE   # state of the simulation (edit or play)
current_simulation_state = SimulationStates.COMPUTING                   # internal state of the simulation (computing or applying states)

is_mouse_Up = True                  # is the mouse up after a click?
targeted_cell = None                # selected cell
previously_targeted_cell = None     # previously selected cell
is_space_pressed = False

while is_simulation_over == False:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:               # EXIT event
        is_simulation_over = True
        
    elif e.type == pygame.KEYUP:            # EDIT/PLAY toggle event
        if e.key == pygame.K_SPACE:
            # make this more elegant dani
            if current_interaction_state == CellularAutomatonExecutionStage.EDIT_MODE:
                current_interaction_state = CellularAutomatonExecutionStage.PLAY_MODE
            else:
                current_interaction_state = CellularAutomatonExecutionStage.EDIT_MODE
            is_space_pressed = True

    elif e.type == pygame.MOUSEBUTTONUP:    # edit mode CELL STATE toggle
        is_mouse_Up = True
        
    pygame.display.update()
    clock.tick(TICK_RATE)
    
    # tick rate testing (background)
    # screen.fill(get_random_color(False))

    # execution of the automata
    if current_interaction_state == CellularAutomatonExecutionStage.PLAY_MODE:

        # ACT DEPENDING THE SIMULATION STATE
        if current_simulation_state == SimulationStates.COMPUTING:
            # if the return of the function is not none is because it just completed all the cells
            if game_of_life.compute_cell_per_cell() != None:
                current_simulation_state = SimulationStates.UPDATING

        elif current_simulation_state == SimulationStates.UPDATING:
            # if the return of the function is not none is because it just completed all the cells
            if game_of_life.update_cell_per_cell() != None:
                current_simulation_state = SimulationStates.COMPUTING
    
    # Automata edit state
    else:

        # mouse primary button pressed
        if pygame.mouse.get_pressed()[0]:
            # get mouse position
            mouse_screen_position = pygame.mouse.get_pos()

            if targeted_cell is not None:   
                previously_targeted_cell = targeted_cell

            targeted_cell = game_of_life.cell_matrix.get_cell_at_pixel(mouse_screen_position[0],mouse_screen_position[1],SCREEN_COMPUTED_SIZE[0],SCREEN_COMPUTED_SIZE[1])
            
            if targeted_cell != None:
                if (is_mouse_Up == True):
                    # targeted_cell.toggle_highlighted_state()
                    targeted_cell.toggle_cell_state()

            is_mouse_Up = False

    # redraw the matrix
    game_of_life.draw_cells(screen)

print ("Exiting window")
pygame.quit()
