#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

class Drinks():

    def __init__(self, naming : str, col : str):
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
        self.name : str = naming

        self.color : str = col

        self.has_alochol: bool = False

        self.has_bubbles : bool = False

        self.is_hot : bool = False

    def setLogic(self, alcohol : bool, bubbles : bool, temp : bool):
        '''
            Set values for has_alcohol, has_bubbles and
            is_hot properties for make object code cleaner.
        '''
        self.has_alcohol  = alcohol

        self.has_bubbles  = bubbles

        self.is_hot = temp

objects : list[Drinks] = []

def drinking(name):
    '''
        Get drink object by name and set first category
        that be more unhealthy if at least one logic
        property is true
    '''
    for obj in objects:
        if name == obj.name:
            return (obj.has_alcohol or obj.has_bubbles or obj.is_hot)
# Define drinks categories and data for show the working
drinking_first = Clasify()

drinking_first.newType('Soda')
drinking_first.newType('Simple Drink')

water = Drinks('Water', 'transparent')

milk = Drinks('Milk', 'white')

lima = Drinks('Lima', 'transparent')
lima.setLogic(False, True, False)

for drink in [water, milk, lima]:
    drinking_first.newValue(drink.name)
    objects.append(drink)

drinking_first.relation(drinking)

drinking_second = Clasify()

drinking_second.newType('Spirit Drink')
drinking_second.newType('Juice')

drinking_third = Clasify()

drinking_third.newType('Infusion')
drinking_third.newType('Juice')

# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')