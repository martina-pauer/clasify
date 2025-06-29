#!/usr/bin/python3
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify

no_real = Clasify()

no_real.new_type('Fantasy')
no_real.new_type('Terror')

some_real = Clasify()

some_real.new_type('Sci-Fi')
some_real.new_type('Realism')

# The path must be complete for get the right file    
os.system('rm -R /workspaces/clasify/src/__pycache__')