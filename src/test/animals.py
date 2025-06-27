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

                Animal.is_it_give_milk, only True for Mammals

                Animal.is_it_crawl, for Reptile is True

                Animal.has_feathers, True for Birds

                Animal.has_gills, for Fish is True

                Animal.is_jelly, for Mollusks is True

                Animal.has_segmented_body, for Arthropods is True
        '''

        self.name : str = naming

        self.is_it_give_milk : bool = False

        self.is_it_crawl : bool = False

        self.has_feathers : bool = False

        self.has_gills : bool = False

        self.is_jelly : bool = False

        self.has_segmented_body : bool = False

def is_mammal(animal_obj : str):
    '''
        Check if animal obj is Mammal or reptile
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj : Animal = obj
            break

    return animal_obj.is_it_give_milk

def is_bird(animal_obj : str):
    '''
        Choose bird or fish
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj : Animal = obj
            break

    return animal_obj.has_feathers

def is_art(animal_obj : str):
    '''
        Choose Arthropods or Mollusks
    '''
    for obj in objects:
        if obj.name == animal_obj:
            animal_obj : Animal = obj
            break

    return animal_obj.has_segmented_body        

# Groups of two categories of animals
first_group, second_group, third_group = Clasify(), Clasify(), Clasify()
# Create animal object for test
cow, python, chicken, rust = Animal('Cow'), Animal('Python'), Animal('Chicken'), Animal('Crustacean')

pla, octopus, alli = Animal('Platypus'), Animal('Octopus'), Animal('Alligator')
mouse, capy = Animal('Mouse'), Animal('Capybara')

cow.is_it_give_milk, capy.is_it_give_milk, python.is_it_give_milk = True, True, False
mouse.is_it_give_milk, pla.is_it_give_milk, alli.is_it_give_milk = True, True, False

chicken.feathers = True
rust.has_segmented_body = True
# Add objects to list for manage names of animals, not object names
objects = objects.__add__([cow, python, rust, chicken, pla, capy, mouse, octopus, alli])
# Set categories in each group
first_group.newType('Mammal')
first_group.newType('Reptile')

for val in ['Cow', 'Mouse', 'Python', 'Platypus', 'Capybara', 'Alligator']:
    first_group.newValue(val)

first_group.relation(is_mammal)

second_group.newType('Bird')
second_group.newType('Fish')

for val in ['Chicken', 'Octopus']:
    second_group.newValue(val)

second_group.relation(is_bird)

third_group.newType('Arthropods')
third_group.newType('Mollusks')

third_group.newValue('Crustacean')
third_group.relation(is_art)
# Join categories groups in a CSV file
for groups in [first_group, second_group, third_group]:
    print(groups.rel)
    groups.getRelation('/workspaces/clasify/data/animals/animals.csv')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')