# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:54:00 2020

@author: Daniel
"""

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
            print ("FILLED")
        else: 
            print ("NOT FILLED")
            
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
        print ("Succesfull addition")
        
