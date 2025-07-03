#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def ocean(name: str):
    '''
        Select America when is in american list
        elsewhere set Europe
    '''
    american_list = open('/workspaces/clasify/data/country/american.txt', 'r')
    is_american = False

    for line in american_list.readlines():
        if line.replace('\n', '') == name:
            is_american = True
            break

    return is_american

def age(name: str):
    '''
        Select Europe or Asia
    '''
    return not ocean(name)

def plants(name: str):
    '''
        Select Africa or Oceania
    '''
    return not ocean(name)

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
atlantic.relation(ocean)
old.relation(age)
jungle.relation(plants)

for each in [atlantic, old, jungle]:
    each.get_relation('/workspaces/clasify/data/country/countries.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')