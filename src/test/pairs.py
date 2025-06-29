#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def mod(val) -> bool:
    '''
        Define clasification conditional code
        for even numbers.
    '''
    # By default is First category at least change
    # only when the value don't fit in the category
    return ((int(val) % 2) != 0)
pairs = Clasify()
# Set the prefix for the data to analize and storage
prefix = '/workspaces/clasify/data/pairs/'
# The current code only clasify even numbers
pairs.get_types(f'{prefix}categories.txt')
pairs.get_values(f'{prefix}values.txt')
pairs.relation(mod)
pairs.get_relation(f'{prefix}relations.csv')
# Show the result
for categories in pairs.rel.keys():
    print(f'Value: {categories}, Category: {pairs.rel[categories.__str__()]}')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')    