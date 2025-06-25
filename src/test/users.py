#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

import re

def getComment(text : str) -> bool:
    '''
        Clasify user comments
    '''
    state = True

    if re.search('[A-Z]+', text):
    # Hater category
        state = True
    elif re.search('[a-z]+', text):
    # Fan category
        state = False
          
    return state

option = 's'

social = Clasify()
# Set all the kinds of user on social media
social.newType('Hater')
social.newType('Fan')
social.newType('Spamer')
# Get all the comments and who have written it
while (option.lower() == 's'):

    comment = input('\n\tWrite comment: ')
    name = input('\tWrite user name: ')
    
    social.newValue(f'{name} : {comment}')

    option = input('Are you wish continue? S/n: ')
# After of get all the comments clasify each one    
social.relation(getComment)

for text in social.rel.keys():
    print(f'[ "{text}" has written by a ({social.rel[text]}) user ]\n')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')