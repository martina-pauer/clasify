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

    state = True

    for object in [avocado]:
        if ((name == object.name) and (object.salt <= object.grease) and (object.sugar <= object.salt) and (object.grease <= object.sugar)):
            state = False
            break

    return state    


data = '/workspaces/clasify/data/foods'

# Clasify objects
health = Clasify()

health.getValues(f'{data}/foods.txt')
health.getTypes(f'{data}/status.txt')

health.relation(foodie)
print(health.rel)
#health.getRelation(f'{data}/foods.csv')

del health
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')