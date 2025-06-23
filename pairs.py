#!/usr/bin/python3
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
# The current code only clasify even numbers
pairs.getTypes('categories.txt')
pairs.getValues('values.txt')
pairs.relation(mod)
pairs.getRelation('relations.csv')
# Show the result
for categories in pairs.rel.keys():
    print(f'Value: {categories}, Category: {pairs.rel[categories.__str__()]}')
