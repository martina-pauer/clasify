#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

# Define conditional functions for clasification
def group_a(data: str):
    '''
        Select Tropical or Arid climate
    '''
    summer = eval(data)

def group_b(data: str):
    '''
        Select Arid or Temperate climate
    '''
    spring = eval(data)

def group_c(data: str):
    '''
        Select Arid or Continental(Polar) climate
    '''
    winter = eval(data)
# Define Clasify objects with climate pairs in the Köppen climate clasification
tropical = Clasify()
arid_temperate = Clasify()
arid_continental = Clasify()
# Set values for that objects (temperature in fahrenheit and monthly rain in inches)
tropical.get_values('/workspaces/clasify/data/koppen/summer.txt')
arid_temperate.get_values('/workspaces/clasify/data/koppen/spring.txt')
arid_continental.get_values('/workspaces/clasify/data/koppen/winter.txt')
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
    each.get_relation('/workspaces/clasify/data/koppen/koppen_climate.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')