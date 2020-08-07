# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:13:29 2020

@author: Daniel
"""

from colors import * 
from Game_Of_Life_Simulation import *
from neighborhood_acquisition_algoritms import *

class NeighborhoodAcquisition:
    
    @staticmethod
    def get_neighborhood(target_cell, cell_matrix, acquisition_algoritm):
        
        # Select a type of neighborhood algorithm to operate with
        
        # get the position of the target cell
        target_cell_x_pos = target_cell.get_position_on_grid()[0]     # x position
        target_cell_y_pos = target_cell.get_position_on_grid()[1]     # y position

        if acquisition_algoritm == NeighborhoodAcquisitionTypes.MOORE:
            return NeighborhoodAcquisition._get_moore_neighborhood(target_cell_x_pos,target_cell_y_pos,cell_matrix)
        else:
            return NeighborhoodAcquisition._get_neumann_neighboorhood(target_cell_x_pos,target_cell_y_pos,cell_matrix)

    @staticmethod
    def _get_neumann_neighboorhood(target_cell_x_pos,target_cell_y_pos, cell_matrix):
        
        output_list = []        # output list with the neighbors

        # compute the teorical position of the neighbors 
        neighbors_positions = []
        neighbors_positions = NeighborhoodAcquisition._perform_neumann_selection(target_cell_x_pos,target_cell_y_pos)

        NeighborhoodAcquisition.remove_invalid_positions(neighbors_positions,cell_matrix)

        # once the not valid positions are removed then get the cells with the targeted coordinates
        for position in neighbors_positions:
            #print (" The type is " + str(type(position)))
            selected_cell = cell_matrix.get_cell(position[0], position[1])

            output_list.append( selected_cell )        # get the cells at those verified positions

        # if there is alist of cells to return then return them
        if len(output_list) != 0:
            return output_list
        else:
            sys.stdout.write(RED)
            print ("ERROR: No cell found to be returned")
            sys.stdout.write(RESET)

    @staticmethod
    def _get_moore_neighborhood(target_cell_x_pos,target_cell_y_pos, cell_matrix):

        output_list = []        # output list with the neighbors

        # compute the teorical position of the neighbors 
        neighbors_positions = []
        neighbors_positions = NeighborhoodAcquisition._perform_moore_selection(target_cell_x_pos,target_cell_y_pos)

        NeighborhoodAcquisition.remove_invalid_positions(neighbors_positions,cell_matrix)

        # once the not valid positions are removed then get the cells with the targeted coordinates
        for position in neighbors_positions:
            #print (" The type is " + str(type(position)))
            selected_cell = cell_matrix.get_cell(position[0], position[1])

            # debug
            # if (target_cell_x_pos == 2 and target_cell_y_pos == 2):
            #     print ("HIGLIGHTING")
            # selected_cell.is_higlighted = True

            output_list.append( selected_cell )        # get the cells at those verified positions
        
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
    def remove_invalid_positions(positions_list, cell_matrix):
        
        index =  0
        for potential_position in positions_list:
            if cell_matrix.check_if_position_inside_matrix(potential_position[0],potential_position[1]):
                positions_list.pop(index)
            
            index += 1

        return positions_list
