#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

def is_age(num):
    '''
        Get all values of age and separate
        by global var age_limit before of
        be second category
    '''
    return (int(num) < age_limit)

age = Clasify()

print('\nClasification by age\n')
# Get categories and separation age between them
first_category = input('\tWrite first category: ')
second_category = input('\tWrite second category: ')
age_limit = int(input(f'\tHow much years need for be "{second_category}"?: '))
# Define categories
age.new_type(first_category)
age.new_type(second_category)
# Show result from 1 to 100 years
for each in range(1, 101):
    age.new_value(each)
# Make relations and output
age.relation(is_age)
age.get_relation(f'data/ages/sub-{age_limit}-{first_category}.csv')
for aging in age.rel.keys():
    print(f'{aging} years is "{age.rel[aging]}"')   
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')