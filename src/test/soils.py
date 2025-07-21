#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def arid(organic_matter: str):
    '''
        Get organic matter percentage greater
        or equal to 60 is Mollisoil elsewhere
        this is Aridisoil
    '''
    return int(organic_matter.replace('%', '')) < 60

def gelli(organic_matter: str):
    '''
        Get organic matter when this is
        not 90% is Gellisoil instead then
        is Oxisoil
    '''
    return int(organic_matter.replace('%', '')) != 90
# Define objects to divide in category pairs    
soiling_first = Clasify()
soiling_second = Clasify()
# Use the USDA soils taxonomy
soiling_first.new_type('Aridisoil')
soiling_first.new_type('Mollisoil')

soiling_second.new_type('Gellisoil')
soiling_second.new_type('Oxisoil')
# Get organic matter percentages from file and clear values [0, 60], [81, 89] and [91, 100]
soiling_second.get_values('/workspaces/clasify/data/soils/organic-matter.txt')
for data in soiling_second.data:
    data = int(data.replace('%', ''))
    if  (
            data <= 60
            or (data >= 81 and data <= 89)
            or (data >= 91 and data <= 100)
        ):
        # Remove from values list invalid for the second object
        soiling_second.data.remove(str(data) + '%')
        # Add new value to first object
        soiling_first.new_value(str(data) + '%')
# Get relation with the data filtered
soiling_first.relation(arid)        
soiling_second.relation(gelli)
# Create CSV file for collect data in the same file
soiling_first.get_relation('/workspaces/clasify/data/soils/soils.csv')
soiling_second.get_relation('/workspaces/clasify/data/soils/soils.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')