#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

import re

def getComment(text : str) -> bool:
    '''
        Clasify user comment in 'Hater', 'Fan' or 'Spam'
    '''
    state = False
    return state

option = 's'

while (option.lower() == 's'):
    comment = input('Write comment: ')
    name = input('Write user name: ')
    option = input('Are you wish continue? S/n: ')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')