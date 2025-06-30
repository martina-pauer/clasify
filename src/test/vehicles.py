#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify


class Vehicle():
    def __init__(self, naming: str, wheels: bool, wings: bool):
        '''
            Get a name, if it has wheels and if it has wings:

                Vehicle.name, name of vehicle

                Vehicle.has_wheels, if it has 1 or more wheels

                Vehicle.has_wings, if it has 1 or more wings pairs
        '''
        self.name: str = naming

        self.has_wheels: bool = wheels

        self.has_wings: bool = wings

def common(moving: str):
    '''
        Water or Ground vehicle
    '''
    for obj in vehicle_objects:
        if moving == obj.name:
            return  (
                        not obj.has_wings
                        and not obj.has_wheels
                    )

def top(moving: str):
    '''
        Select between Ground and Air
    '''
    for obj in vehicle_objects:
        if moving == obj.name:
            return  (
                        not obj.has_wings
                        and obj.has_wheels
                    )        

common_transport = Clasify()
top_transport = Clasify()
# Define common places
common_transport.new_type('Water')
common_transport.new_type('Ground')
# Define top places
top_transport.new_type('Ground')
top_transport.new_type('Air')
# Define transport ways
vehicle_objects =   [
                        Vehicle('Car', True, False),
                        Vehicle('Bus', True, False),
                        Vehicle('Swim', False, False),
                        Vehicle('Plane', False, True),
                        Vehicle('Rocket', False, False),
                        Vehicle('F1', True, False),
                        Vehicle('Boat', False, False),
                    ]
# Load vehicle names in Clasify objects
for each in ['Car', 'Boat', 'Bus', 'Swim']:
    common_transport.new_value(each)
for other in ['Plane', 'Rocket', 'F1']:
    top_transport.new_value(other)    
# Clasify vehicles
common_transport.relation(common)    
top_transport.relation(top)
# Create CSV file with clasification table
common_transport.get_relation('/workspaces/clasify/data/vehicles.csv')
top_transport.get_relation('/workspaces/clasify/data/vehicles.csv')
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')