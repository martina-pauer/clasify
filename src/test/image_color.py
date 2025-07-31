#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PIL import Image
from clasify import Clasify
from colors import warmar

prefix = '/workspaces/clasify'
analize = Clasify()
# Extract color from argument image dir and minimum warming points
source_image = Image.open(sys.argv[1].__str__()).convert('RGB')
minimum = int(sys.argv[2])
# Create difference between has more or les than minimum warming points
analize.new_type(f'Vegetable {minimum.__str__()}')
analize.new_type(f'Fruit {minimum.__str__()}')
# Get the hexadecimal codes and save to the analize object
for width_pixels in range(0, 300):    
    # Analize a reduced image for optimization
    # 300 times with 250 times give 75000 times in total
    for height_pixels in range(0, 250):
        # Extract data from RGB color matrix
        color_code = list(source_image.getpixel((width_pixels, height_pixels)))
        # Color code fixing loop: 225000 iterations
        for block in range(0, 3):
            # This run 3 times with 75000 times give 225000 times in total
            # Convert to hexadecimal color for compatibility with my class
            color_code[block] = hex(color_code[block]).replace('0x', '')
            # Fix digits of each block for get homogeneus hexadecimal codes
            # around 1350000 iterations more
            while color_code[block].__len__() < 2:
                # 225000 * more iterations
                # Add Zeroes when is minor
                color_code[block] = '0' + color_code[block]
            while color_code[block].__len__() > 2:
                # 225000 * more iterations
                # Quit digits when is major
                color_code[block] = color_code[block].replace(color_code[block][0], '')   
        # Use color logic in my class for help to the output    
        color_code = color_code[0] + color_code[1] + color_code[2]
    # Use different data to analize outside of color code fixing loop
    analized = 'organic'
    # From minimum points is first category elsewhere second category
    points = int(color_code[1], 16) + int(color_code[2], 16)    
    # Save value in object in a format useful for the future very descriptive
    analize.new_value(f'#{color_code} has {points} {analized} points and {minimum.__str__()} minimum')    
# Save data from images in a CSV file apart
analize.relation(warmar)
analize.get_relation(f'{prefix}/data/colors/image_data.csv')
source_image.close()
# Clean cache
os.system(f'rm -R {prefix}/src/__pycache__ && rm -R {prefix}/src/test/__pycache__')