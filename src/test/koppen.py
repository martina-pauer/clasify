#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

# Define conditional functions for clasification
def group_a(name: str):
    '''
        Select Tropical or Arid climate
    '''
    pass
def group_b(name: str):
    '''
        Select Arid or Temperate climate
    '''
    pass
def group_c(name: str):
    '''
        Select Arid or Continental climate
    '''
    pass
# Define Clasify objects with climate pairs in the Köppen climate clasification
tropical = Clasify()
arid_temperate = Clasify()
arid_continental = Clasify()
# Set values for that objects (temperature in fahrenheit and monthly rain in inches)
# Set categories
tropical.new_type('Group A: Tropical')
tropical.new_type('Group B: Arid')
arid_temperate.new_type(tropical.data[1])
arid_temperate.new_type('Group C: Temperate')
arid_continental.new_type(tropical.data[1])
arid_continental.new_type('Group D: Continental')
# Clasify objects
tropical.relation(group_a)
arid_temperate.relation(group_b)
arid_continental.relation(group_c)
# Save all in CSV files
for each in [tropical, arid_temperate, arid_continental]:
    each.get_relation('/workspaces/clasify/data/koppen/')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')