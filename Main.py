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


# START PYGAME ------------------------------------------------------------------------------------------------------------------ #

# Initialize Screen

pygame.init()           # INITIALIZE ENGINE

SCREEN_BASE_SIZE = (860,860)
SCREEN_TITLE = "Game_Of_Life"
SCREEN_SIZE_MULTIPLIER = (1,1)
SCREEN_COMPUTED_SIZE = (int(SCREEN_BASE_SIZE[0] * SCREEN_SIZE_MULTIPLIER[0]) ,int(SCREEN_BASE_SIZE[1] * SCREEN_SIZE_MULTIPLIER[1]))
clock = pygame.time.Clock()
TICK_RATE = 10  
is_simulation_over = False

# create the new window
screen = pygame.display.set_mode(( SCREEN_COMPUTED_SIZE[0] ,SCREEN_COMPUTED_SIZE[1]))     # INITIALIZE WINDOW
screen.fill((255, 255, 255))
pygame.display.set_caption(SCREEN_TITLE)

# EXECUTION --------------------------------------------------------------------------------------------------------------------- #
    
ROW_AMOUNT = 50
COLL_AMOUNT = 50

# CREATE THE RULES -------------------------------------------------------------------------------------------------------------- #

simulation_rules = []
simulation_rules.append(Rule("Death by underpopulation",True,True,0,1,False))
simulation_rules.append(Rule("sustainable life",True,True,2,3,True))
simulation_rules.append(Rule("Death by overpopulation",True,True,4,-1,False))     # -1 == infinito a la hora de comprobarlo
simulation_rules.append(Rule("Birth",False,True,3,3,True))

game_of_life_ruleset = Ruleset(simulation_rules)

# CREATE SIMULATION ------------------------------------------------------------------------------------------------------------- #
sys.stdout.write(BLUE)
game_of_life = GameOfLifeSimulation(COLL_AMOUNT, ROW_AMOUNT,SCREEN_COMPUTED_SIZE[0],SCREEN_COMPUTED_SIZE[1],game_of_life_ruleset)

sys.stdout.write(YELLOW + BOLD)     # set the color of the text
print ("Setup performed succesfully")
sys.stdout.write(RESET)             # RESET the color of the text



# # MAIN SYSTEM LOOP
while is_simulation_over == False:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        is_simulation_over = True
    
    pygame.display.update()
    clock.tick(TICK_RATE)
    
    # tick rate testing (background)
    screen.fill(get_random_color(False))


    # apply the rules to the cells
    # game_of_life.compute_cells()
    
    # update the state of the cells
    # game_of_life.update_cells
    
    # redraw the matrix
    # game_of_life.draw_cells(screen)

print ("Exiting window")
pygame.quit()
