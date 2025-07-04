#!/usr/bin/python3

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clasify import Clasify


# Clean cache
os.system('rm -R /workspaces/clasify/src/__pycache__')