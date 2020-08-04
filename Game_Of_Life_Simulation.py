# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:55:40 2020

@author: Daniel
"""
import pygame
import sys
from colors import *

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
        #amount = self.x_size * self.y_size
        amount = len(self._list_Of_Cells)
        return amount
    
    def get_cells(self):
        return self._list_Of_Cells
    
    def add_cell(self,cell_object):
        self._list_Of_Cells.append(cell_object)

        sys.stdout.write(GREEN)
        print ("Succesfull addition")
        sys.stdout.write(RESET)
        
class GridObject:
    
    _position_On_Grid = ()       # position on the grid of objects (x and y)
        
    def __init__(self,position_on_grid):
        self._position_On_Grid = position_on_grid
        
    def get_position(self):
        return self._position_On_Grid


class BinaryCell(GridObject):
    
    cell_id = 0
    is_Filled = False       # is the cell filled? == CELL STATE
    
    under_Update = False    # is the cell being updated?
    under_Compute = False   # is the cell being computed?
    
    _width = 0      # pixels
    _height = 0     # ""
    #_extreme

    def __init__ (self, start_Filled, grid_Position, width, height, cell_id):
        super().__init__(grid_Position)
        
        self.cell_id = cell_id
        
        self._width = width
        self._height = height
        
        # _extreme = grid_Position + (width,height)
        
        self.is_Filled = start_Filled
        
    def print_data (self):
        print ("The cell at: " + ''.join(str(self._position_On_Grid))  + " is ", end = '')        # tuple to string and int to string
        
        if self.is_Filled == True:
            sys.stdout.write(GREEN)
            print ("FILLED")
            sys.stdout.write(RESET)
        else: 
            sys.stdout.write(RED)
            print ("NOT FILLED")
            sys.stdout.write(RESET)
            
    def compute_new_state(self):
        print ("COMPUTING NEW STATE of cell " + str(self.cell_id))
        
        self.is_Filled = not self.is_Filled      # change the state to the inverse
      
    def update_state(self):
        print ("UPDATING STATE " + str(self.cell_id))
        
    def draw(self,screen):
        print ("DRAWING CELL " + str(self.cell_id))
        
        # pygame.draw.rect(_surface,_color,pygame.Rect(_top,_left,_width,_height))
        
        if self.is_Filled:
            pygame.draw.rect(screen,(pygame.Color("black")), pygame.Rect(self._position_On_Grid,(self._width, self._height)))       # square
            # pygame.draw.rect(screen,(pygame.Color("white")), pygame.Rect(self._position_On_Grid,(self._width, self._height)),-20)    # square border
        else:
            pygame.draw.rect(screen,(pygame.Color("white")), pygame.Rect(self._position_On_Grid,(self._width, self._height)))
            # pygame.draw.rect(screen,pygame.Color("black"), pygame.Rect(self._position_On_Grid,(self._width, self._height)),-20)


class GameOfLifeSimulation:

    cell_matrix = CellMatrix((0,0), (0,0), 0, 0)
    
    def __init__(self,x_size, y_size, screen_width, screen_height):
        
        # create the matrix    
        cell_matrix = CellMatrix((0,0), (100,100), y_size, x_size)
        
        # create the cells
        
            # compute cell width and height
        width = screen_width / x_size
        height = screen_height / y_size
                
        # iteration over the X (colls)
        for i_x in range (0,x_size):
            # iterateion over the Y (rows)
            for i_y in range (0, y_size):
                
                x_position = (i_x / (x_size-1)) + width * i_x
                y_position = (i_y / (y_size-1)) + height * i_y
                
                start_filled = (i_x + i_y) % 2
                
                cell_instance = BinaryCell(start_filled,(x_position,y_position),width, height, i_x + i_y)          # create a new cell
                
                cell_matrix.add_cell(cell_instance)              # add the cell to the list
                cell_instance.print_data()
        
        # for i in range (0, x_size * y_size):
             
        #     x_position = 0
        #     y_position = i / (y_size-1) * height
            
        #     cell_instance = BinaryCell(False,(x_position,y_position),width, height)          # create a new cell
        #     cell_matrix.add_cell(cell_instance)              # add the cell to the list
        #     cell_instance.print_data()
            
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
            cell.compute_new_state()
            
    def draw_cells(self, screen):
        sys.stdout.write(LIGHT_GREY)
        print ("DRAWING CELLS")
        sys.stdout.write(RESET)
  
        for cell in self.cell_matrix.get_cells():          
            cell.draw(screen)
            
            

