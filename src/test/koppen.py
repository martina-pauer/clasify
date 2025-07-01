#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

# Define conditional functions for clasification
def group_a(data: str) -> bool:
    '''
        Select Tropical or Arid climate
    '''
    summer = eval(data)
    return (summer[0] >= 64.4 and summer[1] >= 2.4)    

def group_b(data: str) -> bool:
    '''
        Select Arid or Temperate climate
    '''
    spring = eval(data)
    return  (
                (spring[0] > 10 and spring[1] <= 0.66)
                or not group_a(data)
            )

def group_c(data: str) -> bool:
    '''
        Select Arid or Continental(Polar) climate
    '''
    return group_b(data)    
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
arid_continental.new_type(arid_temperate.data[0])
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