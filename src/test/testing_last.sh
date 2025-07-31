#!/bin/bash
# Define minimum score for set the first category as true
MINIMUM_POINTS="180"
# Test colors analyzer with each image
declare -a IMAGE_FILES=(
    "../../data/colors/capybara_temperature_map.png"
    "../../data/colors/heating_map_image-Meta-AI.png"
    "../../data/colors/heating_map_image-ChatGPT-AI.png"
    "../../data/colors/heating_map_image-Google_Gemini-AI.png"
    "../../data/colors/natural_image_surrealist-Google_Gemini-AI.png"
    "../../data/colors/tech_image_cubist-Google_Gemini-AI.png"
)
# Iterating over array is most efficient than repeat the same command many times
for image in "${IMAGE_FILES[@]}"; do
    python3 image_color.py "$image" "$MINIMUM_POINTS"
done    
# Show CSV content from first to last loaded color info
cat -n "../../data/colors/image_data.csv"