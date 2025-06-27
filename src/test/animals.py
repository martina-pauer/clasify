#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

objects = []

class Animal():
    def __init__(self, naming : str):
        '''
            Use a name as paremeter and define
            animal data with boolean properties.

            Boolean properties about an animal:

                Animal.give_milk, only True for Mammals
                Animal., for Reptile is True
                Animal.feathers, True for Birds
                Animal., for Fish is True
        '''
        self.name : str = naming
        self.give_milk : bool = False

def is_mammal(animal_obj):
    '''
        Check if animal obj is Mammal or reptile
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj = obj
            break

    return animal_obj.give_milk
# Groups of two categories of animals
first_group, second_group, third_group, fourth_group = Clasify(), Clasify(), Clasify(), Clasify()
# Create animal object for test
cow, python = Animal('Cow'), Animal('Python')
cow.give_milk, python.give_milk = True, False
# Add objects to list for manage names of animals, not object names
objects = objects.__add__([cow, python])
# Set categories in each group
first_group.newType('Mammal')
first_group.newType('Reptile')

first_group.newValue('Cow')
first_group.newValue('Python')

first_group.relation(is_mammal)
print(first_group.rel)
#second_group.newType('Bird')
#second_group.newType('Fish')

#second_group.relation(is_bird)

# Join categories groups in a CSV file
#for groups in [first_group, second_group, third_group, fourth_group]:
#    groups.getRelation('/workspaces/clasify/data/animals.csv')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')