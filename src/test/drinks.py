#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

class Drinks():

    def __init__(self, naming: str, col: str):
        '''
            Take the drink name and liquid color
            text as parameter for represent drink
            info.

            Properties:
                
                Drinks.name : str, common name for the drink

                Drink.color : str, coloration of drink liquid

                Drink.has_alcohol : bool, say if the drinks is for adults

                Drink.has_bubbles : bool, True for soda drinks

                Drink.is_hot : bool, say if the drink temperature is high
        '''
        self.name: str = naming

        self.color: str = col

        self.has_alcohol: bool = False

        self.has_bubbles: bool = False

        self.is_hot: bool = False

    def set_logic(self, alcohol: bool, bubbles: bool, temp: bool):
        '''
            Set values for has_alcohol, has_bubbles and
            is_hot properties for make object code cleaner.
        '''
        self.has_alcohol  = alcohol

        self.has_bubbles  = bubbles

        self.is_hot = temp

objects: list[Drinks] = []

def drinking(name):
    '''
        Get drink object by name and set first category
        that be more strong if at least one logic
        property is true
    '''
    for obj in objects:
        if name == obj.name:
            return (obj.has_alcohol or obj.has_bubbles or obj.is_hot)
# Define drinks categories and data for show the working
drinking_first = Clasify()

drinking_first.new_type('Soda')
drinking_first.new_type('Simple Drink')

water = Drinks('Water', 'transparent')

milk = Drinks('Milk', 'white')

lima = Drinks('Lima', 'transparent')
lima.set_logic(False, True, False)

for drink in [water, milk, lima]:
    drinking_first.new_value(drink.name)
    objects.append(drink)

drinking_second = Clasify()

drinking_second.new_type('Spirit Drink')
drinking_second.new_type('Juice')

beer = Drinks('Beer', 'golden')
beer.set_logic(True, False, False)

wine = Drinks('Wine', 'light smooth green')
wine.set_logic(True, False, False)

orange = Drinks('Orange Box', 'orange')

for drink in [beer, orange, wine]:
    drinking_second.new_value(drink.name)
    objects.append(drink)

drinking_third = Clasify()

drinking_third.new_type('Infusion')
drinking_third.new_type('Juice')

coffee = Drinks('Coffee Cup', 'Brown')
coffee.set_logic(False, False, True)

mate = Drinks('Argentian Mate', 'Dark Military Green')
mate.set_logic(False, False, True)

tom = Drinks('Tomato Sauce', 'Strong Glowing Red')

for drink in [mate, tom, coffee]:
    drinking_third.new_value(drink.name)
    objects.append(drink)

for drinks in [drinking_first, drinking_second, drinking_third]:
    
    drinks.relation(drinking)
    drinks.get_relation('/workspaces/clasify/data/drinks/drinks.csv')

    for drink in drinks.rel.keys():
        print(f'\n\t{drink} is {drinks.rel[drink]}')    

# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')