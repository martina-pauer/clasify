#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def is_this_america(name: str) -> bool:
    '''
        Select America when is in american list
        elsewhere set Europe
    '''
    american_list = open('/workspaces/clasify/data/country/american.txt', 'r')
    is_american = False

    for state in american_list.readlines():
        if state.replace('\n', '') == name:
            is_american = True
            break

    american_list.close()

    return is_american

def is_this_europe(name: str) -> bool:
    '''
        Select Europe or Asia
    '''
    european_list = open('/workspaces/clasify/data/country/european.txt', 'r')
    is_european = False

    for member in european_list.readlines():
        if member.replace('\n', '') == name:
            is_european = True
            break
        
    european_list.close()    

    return  is_european    

def is_this_africa(name: str) -> bool:
    '''
        Select Africa or Oceania
    '''
    ocean_list = open('/workspaces/clasify/data/country/ocean.txt', 'r')

    is_african = True

    for land in ocean_list.readlines():
        if land.replace('\n', '') == name:
            is_african = False

    ocean_list.close()        
    
    return  is_african

atlantic = Clasify()
old = Clasify()
jungle = Clasify()
# Set categories
atlantic.new_type('America')
atlantic.new_type('Europe')

old.new_type('Europe')
old.new_type('Asia')

jungle.new_type('Africa')
jungle.new_type('Oceania')
# Set values
atlantic.get_values('/workspaces/clasify/data/country/atlantic.txt')
old.get_values('/workspaces/clasify/data/country/old.txt')
jungle.get_values('/workspaces/clasify/data/country/jungle.txt')
# Clasify each one
atlantic.relation(is_this_america)
old.relation(is_this_europe)
jungle.relation(is_this_africa)

for each in [atlantic, old, jungle]:
    each.get_relation('/workspaces/clasify/data/country/countries.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')