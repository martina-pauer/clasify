#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

no_real = Clasify()

no_real.new_type('Fantasy')
no_real.new_type('Terror')

no_real.new_value('The Lord of the Rings')
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