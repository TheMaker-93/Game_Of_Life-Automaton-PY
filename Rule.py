# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:20:17 2020

@author: Daniel
"""

import sys
from neighborhood_acquisition import *
from colors import *
from neighborhood_acquisition_algoritms import *

class Rule:
    
    _name = "not_named"
    
    _selected_cell_filled_state = False
    
    _selected_cell_neighbor_filled_state = False
    _neighbor_min_amount = -1
    _neighbor_max_amount = -1
    
    _selected_cell_end_filled_state = False
    
    def __init__(self,name ,targeted_cell_filled_state,neighbor_cell_filled_state, neighbor_min_amount,neighbor_max_amount, targeted_cell_end_filled_state):
        
        self._name = name
        
        self._selected_cell_filled_state = targeted_cell_filled_state
        
        self._selected_cell_neighbor_filled_state = neighbor_cell_filled_state
        self._neighbor_min_amount = neighbor_min_amount
        self._neighbor_max_amount = neighbor_max_amount
        
        self._selected_cell_end_filled_state = targeted_cell_end_filled_state
        
        sys.stdout.write(GREEN)
        print ("Rule " + str(self._name) + "has been succesfully created" )
        sys.stdout.write(RESET)


    def get_rule_name(self):
        return self._name

    def check_rule(self, targeted_cell, cell_matrix,neighboring_cells):

        print ("Checking cell with index " + str(targeted_cell.cell_id))

        targeted_neighbors_cells = []

        # 1 Check if the targeted cell is on the desired state ( is this rule for this cell¿)
        if targeted_cell.is_filled == self._selected_cell_filled_state:

            # get the neighbors in the state we desire       
            for neighbor in neighboring_cells:
                if bool(neighbor.is_filled) == self._selected_cell_neighbor_filled_state:
                    targeted_neighbors_cells.append(neighbor)

        # 3 Check the amount of neigbors
        targeted_neighbors_count = len(targeted_neighbors_cells)
        if (targeted_neighbors_count >= self._neighbor_min_amount) and (targeted_neighbors_count <= self._neighbor_max_amount):
            return self._selected_cell_end_filled_state       
        # if the rule is not applicable then return the None object (default action)
         

        
class Ruleset:
    
    _rules = []
    
    def __init__(self,rules):
  
        for rule in rules:
            self.add_rule(rule)
        
    def add_rule(self,rule):
        
        self._rules.append(rule)
        
        sys.stdout.write(GREEN)
        print("The rule " + str(rule.get_rule_name()) + " has been added to the ruleset")
        sys.stdout.write(RESET)
        
    def check_rules(self,cell, hosting_cell_matrix):
        
        # 1 Then check the state and amount of neighbors
        neighboring_cells = NeighborhoodAcquisition.get_neighborhood(cell,hosting_cell_matrix,NeighborhoodAcquisitionTypes.MOORE)

        for rule in self._rules:
                      
            sys.stdout.write(RED + BOLD)
            print ("Checking rule: " + rule.get_rule_name())
            new_state = rule.check_rule(cell,hosting_cell_matrix,neighboring_cells)
            sys.stdout.write(RESET)

            #Once a rule has been applied then exit the loop
            # None is the default object returned by any function if no return is set
            # therefore, is the returned value is not null means that the function is returning something, then, the rule could be checked
            # print (str(new_state))
            
            if new_state != None:
                sys.stdout.write(GREEN)
                print ("the new state should be: " + str(new_state)) 
                sys.stdout.write(RESET)
                return new_state
            # else
                # continue with the iteration over the rules

        # if no rule could be applied then just return the same value of the cell passed as input
        return cell.is_filled
            