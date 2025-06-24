#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

class Food():
    def __init__(self, nam : str, sug : float, sal : float):
        '''
            Take as parameter the food name and how
            much sugar and salt has commonly in grams(g).

            Define the food group and how much sugar,
            salt and grass has it.

            Use the method of this class getInfo for a
            readable text with data about the food

            Properties:

                Food.name : str, name of the food

                Food.sugar : float, sugar more common measure (g, grams)

                Food.salt : float, salt more common measure (g, grams)

                Food.grease : float, grease more common measure (g, grams)

                Food.group : str, food group 

                    'Vegetables', 
                    'Grains', 
                    'Protein',
                    'Fruits',
                    'Dairy' 
                    'Starchy', 
                    'Oils'
                    'Legumes'        
        '''
        self.name : str = nam

        self.sugar : float = sug

        self.salt : float = sal

        self.grease : float = 0.00

        self.group : str = 'Fruits'

    def getInfo(self) -> str:    
        '''
            Return a text with a resume of all
            the data of the object
        '''
        return f'\tThe {self.group}-like "{self.name}" has {self.sugar}g of sugar, {self.grease}g of grease and {self.salt}g of salt.'

def foodie(name : str) -> bool:
    '''
        Define foods, compares names and Food object data
        for say if the food is Unhealthy
    '''
    # Avocado of 150g without seed
    avocado = Food('Avocado', 1.00, 0.00)
    avocado.group = 'Oils'
    avocado.grease = 22.00
    
    apple = Food('Apple', 11.10, 0.00)
    apple.group = 'Fruits'
    apple.grease = 0.50

    banana = Food('Banana', 12.80, 0.00)
    banana.group = 'Fruits'
    banana.grease = 0.50

    tomato = Food('Tomato', 2.50, 0.02)
    tomato.group = 'Fruits'
    tomato.grease = 0.30

    egg = Food('Egg', 1.1, 0.31)
    egg.group = 'Protein'
    egg.grease = 9.00

    cow = Food('Meat Cow', 2.00, 3.00)
    cow.group = 'Protein'
    cow.grease = 7.00

    pig = Food('Pig Cow', 12.00, 3.00)
    pig.group = 'Protein'
    pig.grease = 5.00

    fish = Food('Fish', 0.00, 32.00)
    fish.group = 'Protein'
    fish.grease = 0.70

    flour = Food('Flour', 0.00, 0.01)
    flour.group = 'Grains'
    flour.grease = 0.10

    cheese = Food('Cheese', 0.00, 2.42)
    cheese.group = 'Dairy'
    cheese.grease = 25.00

    bread = Food('Bread', 3.40, 0.42)
    bread.group = 'Grains'
    bread.grease = 0.70

    pizza = Food('pizza', 5.00, 10.00)
    pizza.group = 'Dairy'
    pizza.grease = (cheese.grease + tomato.grease + bread.grease)

    state = True

    for object in [avocado, apple, banana, tomato, egg, cow, pig, fish, flour, cheese, bread, pizza]:
        if ((name == object.name) and ((object.salt > object.grease) or (object.salt > object.sugar) or (object.sugar > object.salt) or (object.sugar > object.sugar))):
            state = False
            break

    return state    


data = '/workspaces/clasify/data/foods'

# Clasify objects
health = Clasify()

health.getValues(f'{data}/foods.txt')
health.getTypes(f'{data}/status.txt')

health.relation(foodie)
health.getRelation(f'{data}/foods.csv')

del health
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')