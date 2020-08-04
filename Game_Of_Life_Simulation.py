# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:55:40 2020

@author: Daniel
"""

import sys
from colors import *

class GameOfLifeSimulation:

    def __init__(self,x_size, y_size):
        
        # create the matrix    
        cell_matrix = CellMatrix((0,0), (100,100), y_size, x_size)
        
        # create the cells
        for x in range (0, x_size * y_size):
            cell_instance = BinaryCell(False,(x,x))          # create a new cell
            cell_matrix.add_cell(cell_instance)              # add the cell to the list
            cell_instance.print_data()
            
        # check
        sys.stdout.write(RESET)
        print()
        print ("The amount of cells on the matrix is: " + str(cell_matrix.get_cells_count()))
    
    # Update the state of the cells
    def update_cells(self):       
        for cell in self.cell_matrix:
            cell.update_state()
            
    def compute_cells(self):     
        for cell in self.cell_matrix:
            cell.compute_new_state()
            
class GridObject:
    
    _position_On_Grid = ()       # position on the grid of objects (x and y)
    
    def __init__(self,position_on_grid):
        self._position_On_Grid = position_on_grid
        
    def get_position(self):
        return self._position_On_Grid


class BinaryCell(GridObject):
    
    is_Filled = False       # is the cell filled? == CELL STATE
    
    under_Update = False    # is the cell being updated?
    under_Compute = False   # is the cell being computed?

    def __init__ (self, start_Filled, grid_Position):
        super().__init__(grid_Position)
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
        print ("COMPUTING NEW STATE")
      
    def update_state(self):
        print ("UPDATING STATE")
          

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
        
