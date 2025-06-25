#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

import re

def getComment(text : str) -> bool:
    '''
        Clasify user comments
    '''
    state = False
    return state

option = 's'

social = Clasify()
# Get all the comments and who have written it
while (option.lower() == 's'):

    comment = input('Write comment: ')
    name = input('Write user name: ')
    
    social.newValue(f'{name} : {comment}')

    option = input('Are you wish continue? S/n: ')
# After of get all the comments clasify each one    
social.relation()

for text in social.rel.keys():
    print(f'[ "{text}" is a ({social.rel[text]}) comment ]\n')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')