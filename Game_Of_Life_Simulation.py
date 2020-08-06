# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:55:40 2020

@author: Daniel
"""
import pygame
import sys
from colors import *
from Rule import *

class CellMatrix:
    
    origin_position = ()
    extreme_position = ()
    
    x_size = 0
    y_size = 0
    
    _list_Of_Cells = []      # list with all the binary cells of the system
    
    def __init__(self,origin, extreme, row_amount, coll_amount):       
        self.origin_position = origin
        self.extreme_position = extreme
        self.x_size = coll_amount
        self.y_size = row_amount

    def get_cells_count(self):
        amount = len(self._list_Of_Cells)
        return amount
    
    def get_cells(self):
        return self._list_Of_Cells

    def get_cell_by_index(self, index):
        return self._list_Of_Cells[index]

    def get_cell(self,x_pos,y_pos):
        # convert the x_pos and the y_pos to an index
        id = self.x_size * x_pos + y_pos
        return self.get_cell_by_index(id)
    
    def add_cell(self,cell_object):
        self._list_Of_Cells.append(cell_object)

        sys.stdout.write(GREEN)
        print ("Succesfull addition")
        sys.stdout.write(RESET)

    def check_if_cell_inside_matrix(self,cell_object):
        object_position = (cell_object.get_position_on_grid())
        return self.check_if_position_inside_matrix(object_position[0], object_position[1])

    def check_if_position_inside_matrix(self,x_pos,y_pos):
        if ((x_pos < 0) or (x_pos >= self.x_size)) or ((y_pos < 0) or (y_pos >= self.y_size)):
            return True

        
class GridObject:
    
    _position_on_screen = ()       # position on screen
    _position_on_grid = ()         # integer position inside grid
        
    def __init__(self,position_on_screen, position_on_grid):
        self._position_on_screen = position_on_screen
        self._position_on_grid = position_on_grid
        
    def get_position_on_screen(self):
        return self._position_on_screen

    def get_position_on_grid(self):
        return self._position_on_grid


class BinaryCell(GridObject):
    
    cell_id = 0
    
    is_filled = False       # is the cell filled? == CELL STATE
    next_filled_state = False   # for now the cell holds the new state it will implement once the computations are done (at the update phase)
    
    under_Update = False    # is the cell being updated?
    under_Compute = False   # is the cell being computed?
    
    _width = 0      # pixels
    _height = 0     # ""
    #_extreme

    def __init__ (self, start_Filled, screen_position, grid_position, width, height, cell_id):
        super().__init__(screen_position, grid_position)
        
        self.cell_id = cell_id
        
        self._width = width
        self._height = height
        
        # _extreme = grid_Position + (width,height)
        
        self.is_filled = start_Filled
        
    def print_data (self):
        print ("The cell at: " + ''.join(str(self._position_on_grid))  + " is ", end = '')        # tuple to string and int to string
        
        if self.is_filled == True:
            sys.stdout.write(GREEN)
            print ("\tFILLED")
            sys.stdout.write(RESET)
        else: 
            sys.stdout.write(RED)
            print ("\tNOT FILLED")
            sys.stdout.write(RESET)
            
    def compute_new_state(self, ruleset, hosting_cell_matrix):
        # print ("COMPUTING NEW STATE of cell " + str(self.cell_id))
        
        new_state = ruleset.check_rules(self, hosting_cell_matrix)
        
        self.next_filled_state = new_state
        # self.is_filled = new_state
        # self.is_filled = not self.is_filled      # change the state to the inverse
      
    def update_state(self):
        print ("changing cell state from " + str(self.is_filled) + " to " + str(self.next_filled_state))
        self.is_filled = self.next_filled_state     # update the state with the computed one
        # print ("UPDATING STATE " + str(self.cell_id))
        
    def draw(self,screen):

        if self.is_filled:
            pygame.draw.rect(screen,(pygame.Color("black")), pygame.Rect(self._position_on_screen,(self._width, self._height)))       # square
        else:
            pygame.draw.rect(screen,(pygame.Color("white")), pygame.Rect(self._position_on_screen,(self._width, self._height)))
            pygame.draw.rect(screen,pygame.Color("black"), pygame.Rect(self._position_on_screen,(self._width, self._height)),1)
        
        # blueprint
        # pygame.draw.rect(_surface,_color,pygame.Rect(_top,_left,_width,_height))
        
        


class GameOfLifeSimulation:

    cell_matrix = CellMatrix((0,0), (0,0), 0, 0)
    _ruleset = Ruleset([])
    
    def __init__(self,x_size, y_size, screen_width, screen_height, ruleset):
        
        # create the matrix    
        cell_matrix = CellMatrix((0,0), (100,100), y_size, x_size)
        
        # add the ruleset
        self._ruleset = ruleset
        
        # compute cell width and height
        width = screen_width / x_size
        height = screen_height / y_size
                
        # iteration over the X (colls)
        for i_x in range (0,x_size):
            # iterateion over the Y (rows)
            for i_y in range (0, y_size):
                
                x_position = (i_x / (x_size-1)) + width * i_x
                y_position = (i_y / (y_size-1)) + height * i_y
                
                #start_filled = (i_x + i_y) % 2
                start_filled = (i_x + i_y) % 3
                
                # ------------------------------------------------------------------------------------------ #
                cell_instance = BinaryCell(start_filled,(x_position,y_position),(i_x,i_y),width, height, i_x + i_y)          # create a new cell
                # ------------------------------------------------------------------------------------------ #

                cell_matrix.add_cell(cell_instance)              # add the cell to the list
                cell_instance.print_data()
        
        # check
        sys.stdout.write(RESET)
        print()
        print ("The amount of cells on the matrix is: " + str(cell_matrix.get_cells_count()))
    
    # Update the state of the cells
    def update_cells(self):     
        sys.stdout.write(LIGHT_BLUE)
        print ("UPDATING CELLS")
        sys.stdout.write(RESET)
        
        for cell in self.cell_matrix.get_cells():
            cell.update_state()
            
    def compute_cells(self):
        sys.stdout.write(YELLOW)
        print ("COMPUTING CELLS")
        sys.stdout.write(RESET)
        
        for cell in self.cell_matrix.get_cells():
            cell.compute_new_state(self._ruleset, self.cell_matrix)
            
    def draw_cells(self, screen):
        sys.stdout.write(LIGHT_GREY)
        print ("DRAWING CELLS")
        sys.stdout.write(RESET)
  
        for cell in self.cell_matrix.get_cells():          
            cell.draw(screen)
            
            

