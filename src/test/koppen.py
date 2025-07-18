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
    return  (
                    (summer[0] >= 64.4 and summer[1] >= 2.4)    
                    and not (summer[0] > 50 and summer[1] <= 0.66)
            )           

def group_b(data: str) -> bool:
    '''
        Select Arid or Temperate climate
    '''
    spring = eval(data)
    return      (
                    (spring[0] > 50 and spring[1] <= 0.66)
                    and not (spring[0] <= 64.4 and spring[1] < 1.6)
                )

def group_c(data: str) -> bool:
    '''
        Select Arid or Continental(Polar) climate
    '''
    winter = eval(data)
    return  (
                (winter[0] > 50 and winter[1] <= 0.66)    
                and not (winter[0] > 50 and winter[1] < 1.1811)
            )    
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
arid_temperate.new_type('Group B: Arid')
arid_temperate.new_type('Group C: Temperate')
arid_continental.new_type('Group B: Arid')
arid_continental.new_type('Group D: Continental')
# Clasify objects
tropical.relation(group_a)
arid_temperate.relation(group_b)
arid_continental.relation(group_c)
# Fix comma mistake that make unloadble the CSV file
auxiliar = {}
for trop in tropical.rel.keys():
    auxiliar[trop.replace(', ', '°F average temperature & ').replace('(', '').replace(')', 'in monthly rain')] = tropical.rel[trop]
tropical.rel = auxiliar

auxiliar = {}
for temp in arid_temperate.rel.keys():
    auxiliar[temp.replace(', ', '°F average temperature & ').replace('(', '').replace(')', 'in monthly rain')] = arid_temperate.rel[temp]
arid_temperate.rel = auxiliar

auxiliar = {}
for polar in arid_continental.rel.keys():
    auxiliar[polar.replace(', ', '°F average temperature & ').replace('(', '').replace(')', 'in monthly rain')] = arid_continental.rel[polar]
arid_continental.rel = auxiliar
# Save all in CSV files
for each in [tropical, arid_temperate, arid_continental]:
    each.get_relation('/workspaces/clasify/data/koppen/koppen_climate.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')