#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

import re

obj = Clasify()

def rel(val) -> bool:
    '''
        Make relation for isolated text
    '''
    return True
def is_that_type(text: str) -> bool:
    '''
        Clasify user comments
    '''
    state = False

    if re.search('odio|hate|maldito|mufa|diabolic|fuck|estúpido|stupid|idiot|morir|muere|idiota|disgust|annoying|asco|shame|blame|vergüenza|mierda|shit|basura|fucking|inútil|die|dead|muerte|kill|matar|destruir|destroy|shit|damn|hell|merde|puta|scheiße|cazzo|mierda|puto|verga|fuck|damn|hell|bastard|idiot|stupid', text.lower()):
    # Hater category
        state = True
    elif re.search('bien|genial|good|amo|great|love|gran|buen|felicitaciones|congratulations|excellent|excelente|saludos|encant|like|gusta|happy|feliz|amazing|increible|vida|alegr|happiness|vivir|estupendo|maravilloso|gorgeous|gracias|thank|\U0001F44D', text.lower()):
    # Friendly category
        obj.new_type('Friendly')
        obj.new_value(text)
        obj.relation(rel)
    elif re.search('ofrezco|vendo|vender|compra|(haz mi curso)', text.lower()):
        # Spamer category
        obj.new_type('Spamer')
        obj.new_value(text)
        obj.relation(rel)    

    return state

option = 's'

social = Clasify()
# Set all the kinds of user on social media
social.new_type('Hater')
social.new_value('Spamer')
social.new_value('Friendly')
# Get anew_valueomments and who have written it
while (option.lower() == 's'):

    comment = input('\n\tWrite comment: ')
    name = input('\tWrite user name: ')
    
    social.new_value(f'{name} : {comment}')

    option = input('\nAre you wish continue? S/n: ')
# After of get all the comments clasify each one    
social.relation(is_that_type)
social.rel.update(obj.rel)
social.get_relation('data/users/comments.csv')

print('\nThe user comments are of this way: \n')
for text in social.rel.keys():
    print(f'\t[ "{text}" has written by a ({social.rel[text]}) user ]\n')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')