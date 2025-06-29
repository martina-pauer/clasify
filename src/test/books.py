#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

class Book():
    def __init__(self, name):
        '''
            Define characteristics about a book:

                Book.title : str, book name

                Book.has_fear : bool, if the book is creppy
                
                Book.has_real : bool, some real is in the book

                Book.has_fiction : bool, very much fiction is present in the book

                Book.is_old_time : bool, the history happens in an old time (the past) 
        '''
        self.title: str = name

        self.has_fear: bool = False

        self.has_real: bool = False

        self.has_fiction: bool = False

        self.is_old_time: bool = False    
# Disclaimer: No All books are necessarily reals
objects: list[Book] = [
    Book('The Lord of the Rings: The Ring Fellowship'), Book('Dracula'), Book('Fahrenheit 451'),
    Book('Jeff Bezos Biography'), Book('The Eternaut'), Book('Argentian from XIX century to present'),
    Book('PEP 8 Style Guide'),
    ]

for index in [0, 1, 2, 4]:
    objects[index].has_fiction = True

for index in [3, 5, 6]:
    objects[index].has_real = True

objects[1].has_fear = True

objects[5].is_old_time = True

def fiction(title) -> bool:
    '''
        Conditional function for select Fantasy or Terror
    '''
    for fic in objects:
        if fic.title == title:
            # Haven't mainly terror in the plot
            return not fic.has_fear

def real(title) -> bool:
    '''
        Conditional function for Clasify.relation method
        select Sci-Fi or Realism history
    '''
    for realist in objects:
        if realist.title == title:
            # Happens things that could be happen in a long future
            return realist.has_fiction

def reality(title) -> bool:
    '''
        Select between History or Information (non-fiction educative book)
    '''
    for so_real in objects:
        if so_real.title == title:
            return so_real.is_old_time

no_real = Clasify()

no_real.new_type('Fantasy')
no_real.new_type('Terror')

no_real.new_value('The Lord of the Rings: The Ring Fellowship')
no_real.new_value('Dracula')

some_real = Clasify()

some_real.new_type('Sci-Fi')
some_real.new_type('Realism')

for book in ['Fahrenheit 451', 'Jeff Bezos Biography', 'The Eternaut']:
    some_real.new_value(book)

very_real = Clasify()

very_real.new_type('History')
very_real.new_type('Information')

very_real.new_value('Argentian from XIX century to present')
very_real.new_value('PEP 8 Style Guide')

no_real.relation(fiction)

some_real.relation(real)

very_real.relation(reality)

for books in [no_real, some_real, very_real]:
    books.get_relation('/workspaces/clasify/data/books/books.csv')
# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')