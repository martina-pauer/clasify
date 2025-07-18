#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def is_common(galaxy: str):
    '''
        Select between 'Spiral' or 'Eliptical'
        galaxy shape counting stars
    '''
    stars = float   (
                        galaxy.replace(' ', '').replace('\n', '').split(':')[1]
                    )

    return  (
                stars < 1.2e12
                and stars > 3.0e9
            )

def is_weird(galaxy: str):
    '''
        Select Irregular or Spiral
    '''
    stars = float   (
                        galaxy.replace(' ', '').replace('\n', '').split(':')[1]
                    )
    
    return  (
                stars <= 3.0e9
            )
# Define clasificators
common = Clasify()
weird = Clasify()
# Set common clasification
common.new_type('Spiral')
common.new_type('Eliptical')
# Set weird clasification
weird.new_type('Irregular')
weird.new_type('Spiral')
# Get values with galaxy names and stars count
for obj in     [
                    common,
                    weird,
                ]:
    obj.get_values('/workspaces/clasify/data/galaxy/galaxy.txt')
# Use two kinds of clasification
common.relation(is_common)
weird.relation(is_weird)
# Fragment clasification
common.get_relation('/workspaces/clasify/data/galaxy/galactical_common.csv')
weird.get_relation('/workspaces/clasify/data/galaxy/galactical_weird.csv')
# Merge objects and save results in a file apart
common.merge(weird,     [
                            is_common,
                            is_weird
                         ]
            )
common.get_relation('/workspaces/clasify/data/galaxy/galactical_merging.csv')    
# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')