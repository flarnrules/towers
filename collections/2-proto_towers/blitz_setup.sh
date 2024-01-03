#!/bin/bash

# Configuration variables.
METADATA_DIR="metadata/101-150"
PNG_DIR="media/original_pngs/101-150"
PNG_TEMPLATES_DIR="templates/ms_paint"
JSON_TEMPLATE_DIR="templates/jsons"

# Get the list of PNG templates from the directory.
PNG_TEMPLATES=($(ls $PNG_TEMPLATES_DIR/*.png))

# Check if templates are available.
if [ ${#PNG_TEMPLATES[@]} -eq 0 ]; then
  echo "No PNG templates found in $PNG_TEMPLATES_DIR."
  exit 1
fi

# Prompt the user to select a PNG template.
echo "Available PNG templates:"
for i in "${!PNG_TEMPLATES[@]}"; do
  echo "$((i+1))) $(basename ${PNG_TEMPLATES[i]})"
done
read -p "Select a template (1-${#PNG_TEMPLATES[@]}): " TEMPLATE_NUM

# Validate user input for template selection.
if [ "$TEMPLATE_NUM" -lt 1 ] || [ "$TEMPLATE_NUM" -gt ${#PNG_TEMPLATES[@]} ]; then
  echo "Invalid selection. Please run the script again and select a valid number."
  exit 1
fi

# Adjust index to match array and determine the selected template.
TEMPLATE_INDEX=$((TEMPLATE_NUM-1))
PNG_TEMPLATE=${PNG_TEMPLATES[$TEMPLATE_INDEX]}

# Prompt for the starting and ending ID numbers.
read -p "Enter the starting ID number: " START_NUM
read -p "Enter the ending ID number: " END_NUM

# Validate user input for ID numbers.
if ! [[ "$START_NUM" =~ ^[0-9]+$ ]] || ! [[ "$END_NUM" =~ ^[0-9]+$ ]] || [ "$START_NUM" -ge "$END_NUM" ]; then
  echo "Invalid input. Starting ID should be a number, less than the ending ID number."
  exit 1
fi

# Loop through the range and create copies with updated names.
for i in $(seq $START_NUM $END_NUM); do
    # Copy and rename the metadata JSON file.
    JSON_FILE="$METADATA_DIR/$i.json"
    cp "$JSON_TEMPLATE_DIR/blitz_template.json" "$JSON_FILE"

    # Update the "name" field in the JSON file.
    jq --arg name "Proto Tower $i" '.name = $name' "$JSON_FILE" > temp.json && mv temp.json "$JSON_FILE"

    # Copy and rename the selected PNG file.
    cp "$PNG_TEMPLATE" "$PNG_DIR/$i.png"
done

echo "Blitz deployment setup complete for IDs $START_NUM to $END_NUM using $(basename $PNG_TEMPLATE)."
