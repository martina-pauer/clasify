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

    if re.search('([A-Z]+|odio|hate|maldito|mufa|diabolic|fuck|estúpido|stupid|idiot|idiota|disgust|annoying|asco|shame|blame|vergüenza|mierda|shit|basura|fucking|inútil|die|dead|muerte|kill|matar|destruir|destroy|\b[a-zA-Z0-9]*f[u|ú]ck\b|\b[a-zA-Z0-9]*shit\b|\b[a-zA-Z0-9]*damn\b|\b[a-zA-Z0-9]*hell\b|[А-Яа-яЁё]*бля[А-Яа-яЁё]*|\b[a-zA-Z0-9]*merde\b|\b[a-zA-Z0-9]*puta\b|\b[a-zA-Z0-9]*con\b|[a-zA-Z0-9]*scheiße[a-zA-Z0-9]*|\b[a-zA-Z0-9]*cazzo\b|[a-zA-Z0-9]*mierda[a-zA-Z0-9]*|[a-zA-Z0-9]*puto[a-zA-Z0-9]*|[a-zA-Z0-9]*verga[a-zA-Z0-9]*|\b[a-zA-Z0-9]*fuck\b|\b[a-zA-Z0-9]*damn\b|\b[a-zA-Z0-9]*hell\b|\b[a-zA-Z0-9]*bastard\b|\b[a-zA-Z0-9]*idiot\b|\b[a-zA-Z0-9]*stupid\b|[A-ZÁÉÍÓÚÜÑ]{3,}|[!¡?¿]{2,})', text):
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

    option = input('\nAre you wish continue? S/n: ')
# After of get all the comments clasify each one    
social.relation(getComment)

print('\nThe user comments are of this way: \n')
for text in social.rel.keys():
    print(f'\t[ "{text}" has written by a ({social.rel[text]}) user ]\n')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')