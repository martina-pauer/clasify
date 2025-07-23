#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PIL import Image
from clasify import Clasify
from colors import Color
from colors import warmar

prefix = '/workspaces/clasify'
analize = Clasify()
# Extract color from argument image dir and minimum warming points
source_image = Image.open(sys.argv[1].__str__()).convert('RGB')
minimum = int(sys.argv[2])
# Create difference between has more or les than minimum warming points
analize.new_type(f'Hight Temperature (warm) {minimum.__str__()}')
analize.new_type(f'Low Temperature (cold) {minimum.__str__()}')
# Get the hexadecimal codes and save to the analize object
for width_pixels in range(0, source_image.width + 1):
    for height_pixels in range(0, source_image.height + 1):
        # Extract data from RGB color matrix
        color_code = source_image.getpixel((width_pixels, height_pixels))
        for block in range(0, color_code.__len__()):
            # Convert to hexadecimal color for compatibility with my class
            color_code[block] = hex(color_code[block]).replace('0x', '')
        # Use color logic in my class for help to the output    
        palette  = Color(color_code[0] + color_code[1] + color_code[2])
        palette.warm(minimum)
        # Save value in object in a format useful for the future very descriptive    
        analize.new_value(f'#{color_code} has {palette.warming_points} warming points and {minimum.__str__()} minimum')    
# Save data from images in a CSV file apart
analize.relation(warmar)
analize.get_relation(f'{prefix}/data/colors/image_data.csv')
source_image.close()
# Clean cache when is no needed more
os.system(f'rm -R {prefix}/src/__pycache__')