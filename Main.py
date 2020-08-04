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

# EXECUTION --------------------------------------------------------------------------------------------------------------------- #
    
ROW_AMOUNT = 10
COLL_AMOUNT = 10
AMOUNT_OF_INSTANCES = ROW_AMOUNT * COLL_AMOUNT

# CREATE THE RULES -------------------------------------------------------------------------------------------------------------- #
simulation_rules = []
rule = Rule("New Rule",1,0,1,5,1)


# CREATE SIMULATION ------------------------------------------------------------------------------------------------------------- #
sys.stdout.write(BLUE)
game_of_life = GameOfLifeSimulation(COLL_AMOUNT, ROW_AMOUNT)

sys.stdout.write(YELLOW + BOLD)     # set the color of the text
print ("Setup performed succesfully")
sys.stdout.write(RESET)             # RESET the color of the text


# START PYGAME ------------------------------------------------------------------------------------------------------------------ #

# Initialize Screen

pygame.init()           # INITIALIZE ENGINE

SCREEN_BASE_SIZE = (1920,1920)
SCREEN_TITLE = "Game_Of_Life"
SCREEN_SIZE_MULTIPLIER = (0.5,0.5)
SCREEN_COMPUTED_SIZE = (int(SCREEN_BASE_SIZE[0] * SCREEN_SIZE_MULTIPLIER[0]) ,int(SCREEN_BASE_SIZE[1] * SCREEN_SIZE_MULTIPLIER[1]))
clock = pygame.time.Clock()
TICK_RATE = 2  
is_simulation_over = False

# create the new window
screen = pygame.display.set_mode(( SCREEN_COMPUTED_SIZE[0] ,SCREEN_COMPUTED_SIZE[1]))     # INITIALIZE WINDOW
screen.fill((255,255,255))
pygame.display.set_caption(SCREEN_TITLE)


# # MAIN SYSTEM LOOP
while is_simulation_over == False:
    
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        is_simulation_over = True
    
    pygame.display.update()
    clock.tick(TICK_RATE)
    
    screen.fill(get_random_color(False))
        

"""
while True:
    
    # itearate throught all the cells and draw them
    # game_of_life.draw_cells()
    
    
    # window closing event
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break;
"""

print ("Exiting window")
pygame.quit()
