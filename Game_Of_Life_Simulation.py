# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:55:40 2020

@author: Daniel
"""
import pygame
import sys
from Cell_State import CellState
from colors import ConsoleColor
from colors import get_random_color
from Rule import Ruleset
from random import randint
from Cell_Simulation_Stages import CellSimulationStages

class CellMatrix:
    
    origin_position = ()
    extreme_position = ()
    
    coll_amount = -1
    row_amount = -1
    
    _list_Of_Cells = []      # list with all the binary cells of the system

    def __init__(self,origin, extreme, row_amount, coll_amount):       
        self.origin_position = origin
        self.extreme_position = extreme
        self.coll_amount = coll_amount
        self.row_amount = row_amount

    def get_cells_count(self):
        amount = len(self._list_Of_Cells)
        return amount
    
    def get_cells(self):
        return self._list_Of_Cells

    def print_cells_data(self):
        for cell in self._list_Of_Cells:
            cell.print_data()

    def get_cell_by_index(self, index):
        # print ("Getting cell with index " + str(index))
        return self._list_Of_Cells[index]

    def get_cell(self,x_pos,y_pos):
        # convert the x_pos and the y_pos to an index    
        id = self.get_cell_index(x_pos,y_pos)
        # print ("with x position being: " + str(x_pos) + " and y position: " + str(y_pos) + " the resulting id is" +str(id))
        return self.get_cell_by_index(id)
    
    def get_cell_index(self,x_pos,y_pos):
        # Id = Current Row * Matrix Width + Current Coll
        return y_pos * self.coll_amount + x_pos
          
    def get_cell_at_pixel(self,x_pixel, y_pixel, screen_width, screen_height):
        
        # x position in grid is equal to the pixel x coordindate / width in pixels of the cells
        x_grid_posiion = x_pixel / (screen_width / self.coll_amount)
        y_grid_position = y_pixel / (screen_height / self.row_amount)
        
        selected_cell = self.get_cell(int(x_grid_posiion), int(y_grid_position))
        if (selected_cell == None):
            print ("No cell found for the pixel at x: " + str(x_pixel) + " y: " + str(y_pixel))
        
        return selected_cell

    def add_cell(self,cell_object):
        self._list_Of_Cells.append(cell_object)

    def check_if_cell_inside_matrix(self,cell_object):
        
        object_position = (cell_object.get_position_on_grid())
        inside = self.check_if_position_inside_matrix(object_position[0], object_position[1])

        return inside


    def check_if_position_inside_matrix(self,x_pos,y_pos):
        
        if (x_pos < 0 or x_pos >= self.coll_amount) or (y_pos < 0 or y_pos >= self.row_amount):
            return False
        else:
            return True
        
class GridObject:
    
    _position_on_screen = ()       # position on screen
    _position_on_grid = ()         # integer position inside grid
        
    def __init__(self,position_on_screen, position_on_grid):
        print (str(position_on_screen) + " " + str(position_on_grid))
        self._position_on_screen = position_on_screen
        self._position_on_grid = position_on_grid
        
    def get_position_on_screen(self):
        return self._position_on_screen

    def get_position_on_grid(self):
        return self._position_on_grid


class BinaryCell(GridObject):
    
    cell_id = 0
    
    state = CellState.NOT_DEFINED
    next_state = CellState.NOT_DEFINED

    under_Update = False    # is the cell being updated?
    under_Compute = False   # is the cell being computed?
    
    _width = 0      # pixels
    _height = 0     # ""

    _is_highlighted = False

    _cell_simulation_stage = CellSimulationStages.IDLE

    def __init__ (self, start_cell_state, screen_position, grid_position, width, height, cell_id):
        super().__init__(screen_position, grid_position)
        
        self.cell_id = cell_id
        
        self._width = width
        self._height = height
        
        self.state = start_cell_state
        
    def set_cell_simulation_stage(self, new_simulation_stage):

        sys.stdout.write(ConsoleColor.BLUE)
        print ("Setting state: " + new_simulation_stage.name + " to the cell " + str(self.cell_id))
        sys.stdout.write(ConsoleColor.RESET)

        self._cell_simulation_stage = new_simulation_stage

    def reset_visual_cues(self):
        self._is_highlighted = False

    def set_highlighted_state(self, new_state):
        self._is_highlighted = new_state
    
    def toggle_highlighted_state(self):
        self._is_highlighted = not self._is_highlighted

    def get_highlighted(self):
        return self._is_highlighted

    def print_data (self):
        print ("The cell at: " + ''.join(str(self._position_on_grid))  + " is: ", end = '')        # tuple to string and int to string
        
        if self.state == CellState.FILLED:
            sys.stdout.write(ConsoleColor.GREEN)
            print ("\tFILLED")
            sys.stdout.write(ConsoleColor.RESET)
        elif self.state == CellState.EMPTY: 
            sys.stdout.write(ConsoleColor.RED)
            print ("\tNOT FILLED")
            sys.stdout.write(ConsoleColor.RESET)
            
    def compute_new_state(self, ruleset, hosting_cell_matrix):
        # print ("COMPUTING NEW STATE of cell " + str(self.cell_id))    
        self.set_cell_simulation_stage(CellSimulationStages.COMPUTING)
        self.next_state = ruleset.check_rules(self, hosting_cell_matrix)

    def toggle_cell_state(self):

        # make this more elegant
        if self.state == CellState.FILLED:
            self.state = CellState.EMPTY
        elif self.state == CellState.EMPTY:
            self.state = CellState.FILLED

    def update_state(self):
        print ("changing cell state from " + str(self.state.name) + " to " + str(self.next_state.name))     
        self.set_cell_simulation_stage(CellSimulationStages.UPDATING) 
        self.state = self.next_state
        
    def draw(self,screen):

        # blueprint:
        # pygame.draw.rect(_surface,_color,pygame.Rect(_top,_left,_width,_height))
        
        if self.state == CellState.FILLED:
            pygame.draw.rect(screen,(pygame.Color("black")), pygame.Rect(self._position_on_screen,(self._width, self._height)))       # square
        elif self.state == CellState.EMPTY:
            pygame.draw.rect(screen,(pygame.Color("white")), pygame.Rect(self._position_on_screen,(self._width, self._height)))
            pygame.draw.rect(screen,pygame.Color("black"), pygame.Rect(self._position_on_screen,(self._width, self._height)),1)
        elif self.state == CellState.NOT_DEFINED:
            pygame.draw.rect(screen,(pygame.Color("red")), pygame.Rect(self._position_on_screen,(self._width, self._height)))       # square

        if self._is_highlighted:
            pygame.draw.rect(screen,(pygame.Color("orange")), pygame.Rect(self._position_on_screen ,(self._width*0.8, self._height*0.8)))       # square

        if self._cell_simulation_stage != CellSimulationStages.IDLE:

            if self._cell_simulation_stage == CellSimulationStages.UPDATING:
                pygame.draw.rect(screen,(pygame.Color("green")), pygame.Rect(self._position_on_screen ,(self._width*0.8, self._height*0.8)))       # square
            elif self._cell_simulation_stage == CellSimulationStages.COMPUTING:
                pygame.draw.rect(screen,(pygame.Color("blue")), pygame.Rect(self._position_on_screen ,(self._width*0.8, self._height*0.8)))       # square




class GameOfLifeSimulation:

    cell_matrix = CellMatrix((0,0), (0,0), 0, 0)
    _ruleset = Ruleset([])

    # for the iteration cell per cell
    _current_iteration_index = 0

    _current_cell_being_computed = None
    _current_cell_being_updated = None
    
    def __init__(self,coll_amount, row_amount, screen_width, screen_height, ruleset):

        # create the matrix    
        self.cell_matrix = CellMatrix((0,0), (screen_width,screen_height), row_amount, coll_amount)
        
        # add the ruleset
        self._ruleset = ruleset
        
        # compute cell width and height
        width = screen_width / coll_amount
        height = screen_height / row_amount
                
        # iteration over the X (colls)
        for row in range (0,coll_amount):
            # iterateion over the Y (rows)
            for coll in range (0, row_amount):
                
                x_position = (coll / (coll_amount-1)) + width * coll
                y_position = (row / (row_amount-1)) + height * row

                start_cell_state = CellState(randint(0,1))
                
                # ------------------------------------------------------------------------------------------ #
                cell_instance = BinaryCell(start_cell_state,(x_position,y_position),(coll,row),width, height, row * coll_amount + coll)          # create a new cell
                # ------------------------------------------------------------------------------------------ #

                self.cell_matrix.add_cell(cell_instance)              # add the cell to the list
                cell_instance.print_data()
        
        # check
        sys.stdout.write(ConsoleColor.RESET)
        print()
        print ("The amount of cells on the matrix is: " + str(self.cell_matrix.get_cells_count()))
        sys.stdout.write(ConsoleColor.RESET)

    # Update the state of the cells
    def update_cells(self):     
        sys.stdout.write(ConsoleColor.LIGHT_BLUE)
        print ("UPDATING CELLS")
        sys.stdout.write(ConsoleColor.RESET)
        
        for cell in self.cell_matrix.get_cells():

            # reset the state of the previously computed cell if there is none
            if (self._current_cell_being_updated != None):
                self._current_cell_being_updated.set_cell_simulation_stage(CellSimulationStages.IDLE)

            # set the new cell as under update
            self._current_cell_being_updated = cell

            cell.update_state()
            
    def compute_cells(self):
        sys.stdout.write(ConsoleColor.YELLOW)
        print ("COMPUTING CELLS")
        sys.stdout.write(ConsoleColor.RESET)
        
        for cell in self.cell_matrix.get_cells():

            if (self._current_cell_being_computed != None):
                self._current_cell_being_computed.set_cell_simulation_stage(CellSimulationStages.IDLE)

            self._current_cell_being_computed = cell

            cell.compute_new_state(self._ruleset, self.cell_matrix)
            
    def compute_cell_per_cell(self):
        
        # If computing the cells we see there is a cell still without being reset in terms of state then we reset it
        if self._current_iteration_index == 0 and self._current_cell_being_updated != None:
            self._current_cell_being_updated.set_cell_simulation_stage(CellSimulationStages.IDLE)

        if (self._current_cell_being_computed != None):
            self._current_cell_being_computed.set_cell_simulation_stage(CellSimulationStages.IDLE)

        cell_to_compute = self.cell_matrix.get_cell_by_index(self._current_iteration_index)
        self._current_cell_being_computed = cell_to_compute
        
        cell_to_compute.compute_new_state(self._ruleset, self.cell_matrix)
        
        self._current_iteration_index += 1

        # if current is last index restart
        if (self._current_iteration_index >= self.cell_matrix.get_cells_count()):
            self._current_iteration_index = 0
            return True
        
    def update_cell_per_cell(self):

        # If updating the cells we see there is a cell still without being reset in terms of state then we reset it
        if self._current_iteration_index == 0 and self._current_cell_being_computed != None:
            self._current_cell_being_computed.set_cell_simulation_stage(CellSimulationStages.IDLE)

        if (self._current_cell_being_updated != None):
            self._current_cell_being_updated.set_cell_simulation_stage(CellSimulationStages.IDLE)

        sys.stdout.write(ConsoleColor.YELLOW)
        print (self._current_iteration_index)
        sys.stdout.write(ConsoleColor.RESET)

        cell_to_update = self.cell_matrix.get_cell_by_index(self._current_iteration_index)
        self._current_cell_being_updated = cell_to_update
        
        cell_to_update.update_state()
        
        #cell_to_update._is_highlighted = True
        self._current_iteration_index += 1

        # if current is last index restart
        if (self._current_iteration_index >= self.cell_matrix.get_cells_count()):
            self._current_iteration_index = 0
            return True

    def draw_cells(self, screen):
        # sys.stdout.write(ConsoleColor.LIGHT_GREY)
        # print ("DRAWING CELLS")
        # sys.stdout.write(ConsoleColor.RESET)
  
        for cell in self.cell_matrix.get_cells():          
            cell.draw(screen)
            
            

