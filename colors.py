# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:15:33 2020

@author: Daniel
"""

from random import randrange


# Colors used by sys.stdout.write

BLACK = "\033[0;30m"
LIGHT_GREY = "\033[0;37m"
DARK_GREY = "\033[1;30m"
RED   = "\033[1;31m"  
LIGHT_RED = "\033[1;31m"
BLUE  = "\033[1;34m"
LIGHT_BLUE = "\033[1;34m"
CYAN  = "\033[1;36m"
LIGHT_CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
PURPLE = "\033[0;35m"
LIGHT_PURPLE = "\033[1;35m"
BROWN = "\033[0;33m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"

RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

"""
       Negro       0;30     Gris oscuro    1;30
       Azul        0;34     Azul claro     1;34
       Verde       0;32     Verde claro    1;32
       Cyan        0;36     Cyan claro     1;36
       Rojo        0;31     Rojo claro     1;31
       Purpura     0;35     Purpura claro  1;35
       Marron      0;33     Amarillo       1;33
       Gris claro  0;37     blanco         1;37

"""

def get_random_color(include_alpha):
    
    red = randrange(255)
    green = randrange(255)
    blue = randrange(255)
    alpha = 255
    
    if (include_alpha):
        alpha = randrange(255)
    
    return (red,green,blue,alpha)
    