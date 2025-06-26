#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

import re

def is_that_type(text : str) -> bool:
    '''
        Clasify user comments
    '''
    state = True

    if re.search('odio|hate|maldito|mufa|diabolic|fuck|estúpido|stupid|idiot|idiota|disgust|annoying|asco|shame|blame|vergüenza|mierda|shit|basura|fucking|inútil|die|dead|muerte|kill|matar|destruir|destroy|shit|damn|hell|[a-zA-Z0-9]*merde|[a-zA-Z0-9]*puta|[a-zA-Z0-9]*con|[a-zA-Z0-9]*scheiße[a-zA-Z0-9]*|[a-zA-Z0-9]*cazzo|[a-zA-Z0-9]*mierda[a-zA-Z0-9]*|[a-zA-Z0-9]*puto[a-zA-Z0-9]*|[a-zA-Z0-9]*verga[a-zA-Z0-9]*|[a-zA-Z0-9]*fuck|[a-zA-Z0-9]*damn|[a-zA-Z0-9]*hell|[a-zA-Z0-9]*bastard|[a-zA-Z0-9]*idiot|stupid', text):
    # Hater category
        state = True
    elif re.search('bien|genial|good|great|love|gran|[a-zA-Z0-9]+|[a-zA-Z0-9áéíóúüñÁÉÍÓÚÜÑ.,?!]+|buen|felicitaciones|congratulations|excellent|excelente|saludos|encant|like|gusta|happy|feliz|amazing|increible|vida|alegr|happiness|vivir|estupendo|maravilloso|gorgeous|gracias|thank|\U0001F44D', text):
    # Friendly category
        state = False

    return state

option = 's'

social = Clasify()
# Set all the kinds of user on social media
social.newType('Hater')
social.newType('Friendly')
social.newType('Spamer')
# Get all the comments and who have written it
while (option.lower() == 's'):

    comment = input('\n\tWrite comment: ')
    name = input('\tWrite user name: ')
    
    social.newValue(f'{name} : {comment}')

    option = input('\nAre you wish continue? S/n: ')
# After of get all the comments clasify each one    
social.relation(is_that_type)
#social.getRelation('data/comments.csv')

print('\nThe user comments are of this way: \n')
for text in social.rel.keys():
    print(f'\t[ "{text}" has written by a ({social.rel[text]}) user ]\n')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')