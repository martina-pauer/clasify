#!/usr/bin/bash
# Define minimum score for set the first category as true
MINIMUM_POINTS=3499525
# Test colors analyzer with each image
./image_color.py "../../data/colors/capybara_temperature_map.png" $MINIMUM_POINTS
./image_color.py "../../data/colors/heating_map_image-Meta-AI.png" $MINIMUM_POINTS
./image_color.py "../../data/colors/heating_map_image-ChatGPT-AI.png" $MINIMUM_POINTS
./image_color.py "../../data/colors/heating_map_image-Google_Gemini-AI.png" $MINIMUM_POINTS
./image_color.py "../../data/colors/natural_image_surrealist-Google_Gemini-AI.png" $MINIMUM_POINTS
./image_color.py "../../data/colors/tech_image_cubist-Google_Gemini-AI.png" $MINIMUM_POINTS
# Show CSV content from first to last loaded color info
cat -n "../../data/colors/image_data.csv"