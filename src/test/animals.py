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
                Animal.crawl, for Reptile is True
                Animal.feathers, True for Birds
                Animal.gills, for Fish is True
        '''

        self.name : str = naming

        self.give_milk : bool = False

        self.crawl : bool = False

        self.feathers : bool = False

        self.gills : bool = False

def is_mammal(animal_obj : Animal):
    '''
        Check if animal obj is Mammal or reptile
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj = obj
            break

    return animal_obj.give_milk

def is_bird(animal_obj : Animal):
    '''
        Choose bird or fish
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj = obj
            break

    return animal_obj.feathers    

# Groups of two categories of animals
first_group, second_group, third_group, fourth_group = Clasify(), Clasify(), Clasify(), Clasify()
# Create animal object for test
cow, python, chicken = Animal('Cow'), Animal('Python'), Animal('Chicken')
cow.give_milk, python.give_milk = True, False
chicken.feathers = True
# Add objects to list for manage names of animals, not object names
objects = objects.__add__([cow, python, chicken])
# Set categories in each group
first_group.newType('Mammal')
first_group.newType('Reptile')

first_group.newValue('Cow')
first_group.newValue('Python')

first_group.relation(is_mammal)
print(first_group.rel)
second_group.newType('Bird')
second_group.newType('Fish')

second_group.newValue('Chicken')
second_group.relation(is_bird)
print(second_group.rel)
# Join categories groups in a CSV file
#for groups in [first_group, second_group, third_group, fourth_group]:
#    groups.getRelation('/workspaces/clasify/data/animals.csv')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')