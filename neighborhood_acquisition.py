# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:13:29 2020

@author: Daniel
"""

from colors import * 
from Game_Of_Life_Simulation import *
from neighborhood_acquisition_algoritms import *

class NeighborhoodAcquisition:

    returned_cells = []

    @staticmethod   # Select a type of neighborhood algorithm to operate with
    def get_neighborhood(target_cell, cell_matrix, acquisition_algoritm):
        
        output_list = []        # output list with the neighbors

        if (NeighborhoodAcquisition.returned_cells != None):
            for cell in NeighborhoodAcquisition.returned_cells:
                cell.set_highlighted_state(False)
        
        # get the position of the target cell
        target_cell_x_pos = target_cell.get_position_on_grid()[0]     # x position
        target_cell_y_pos = target_cell.get_position_on_grid()[1]     # y position

        neighbors_positions = []
        if acquisition_algoritm == NeighborhoodAcquisitionTypes.MOORE:
            neighbors_positions = NeighborhoodAcquisition._perform_moore_selection(target_cell_x_pos,target_cell_y_pos)
        else:
            neighbors_positions = NeighborhoodAcquisition._perform_neumann_selection(target_cell_x_pos,target_cell_y_pos)

        # debug ---------------------------------------------------
        sys.stdout.write(YELLOW)
        print ("For the cell at position " + str(target_cell_x_pos) + " " + str(target_cell_y_pos) + " you are targeting: ", end = '')
        sys.stdout.write(BLUE)
        for position in neighbors_positions:
            print ("\t x: " + str(position[0]) + "\t y: " + str(position[1]))
        sys.stdout.write(RESET)

        # hasta aqui correcto

        # remove out of range positions
        NeighborhoodAcquisition.remove_out_of_bounds_positions(neighbors_positions,cell_matrix)

        sys.stdout.write(GREEN)
        print ("For the cell at position AND AFTER CLEAN UP" + str(target_cell_x_pos) + " " + str(target_cell_y_pos) + " you are targeting: \n", end = '')
        for position in neighbors_positions:
            print ("\t x: " + str(position[0]) + "\t y: " + str(position[1]))
        sys.stdout.write(RESET)

        # once the not valid positions are removed then get the cells with the targeted coordinates
        output_list = NeighborhoodAcquisition._get_cells_from_positions(neighbors_positions,cell_matrix)
        NeighborhoodAcquisition.returned_cells = output_list

        for cell in output_list:
            cell.set_highlighted_state(True)

        # if there is alist of cells to return then return them
        if len(output_list) != 0:
            return output_list
        else:
            sys.stdout.write(RED)
            print ("ERROR: No cell found to be returned")
            sys.stdout.write(RESET)

    @staticmethod
    def _perform_moore_selection(target_cell_x_pos,target_cell_y_pos):
        
        neighbors_positions = []
        neighbors_positions = NeighborhoodAcquisition._perform_neumann_selection(target_cell_x_pos,target_cell_y_pos)
        
        neighbors_positions.append((target_cell_x_pos - 1,target_cell_y_pos- 1))     # top left
        neighbors_positions.append((target_cell_x_pos + 1, target_cell_y_pos +1))    # bottom right 
        neighbors_positions.append((target_cell_x_pos + 1, target_cell_y_pos - 1))    # top right
        neighbors_positions.append((target_cell_x_pos - 1, target_cell_y_pos + 1))    # bottom left

        return neighbors_positions

    @staticmethod
    def _perform_neumann_selection(target_cell_x_pos,target_cell_y_pos):

        neighbors_positions = []

        neighbors_positions.append((target_cell_x_pos - 1,target_cell_y_pos))     # left cell
        neighbors_positions.append((target_cell_x_pos + 1, target_cell_y_pos))    # right cell
        neighbors_positions.append((target_cell_x_pos, target_cell_y_pos - 1))    # top cell
        neighbors_positions.append((target_cell_x_pos, target_cell_y_pos + 1))    # bottom cell

        return neighbors_positions
    
    @staticmethod
    def remove_out_of_bounds_positions(positions_list, cell_matrix):
        
        index =  0
        for potential_position in positions_list:
            if cell_matrix.check_if_position_inside_matrix(potential_position[0],potential_position[1]) == False:
                
                sys.stdout.write(RED)
                print ("\tRemoving position: " + str(potential_position))

                positions_list.pop(index)
            
            index += 1

        return positions_list

    @staticmethod
    def _get_cells_from_positions(positions_list, cell_matrix):

        output_list = []

        for position in positions_list:
            selected_cell = cell_matrix.get_cell(position[0], position[1])
            output_list.append( selected_cell )        # get the cells at those verified positions

        return output_list