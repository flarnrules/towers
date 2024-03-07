#!/bin/bash

# Configuration variables.
METADATA_DIR="templates/jsons"
ASEPRITE_DIR="templates/aseprite"
DEST_JSON_DIR="metadata/201-250"
DEST_ASEPRITE_DIR="media/aseprite/201-250"
ASEPRITE_TEMPLATES=("8x8.aseprite" "16x16.aseprite" "32x32.aseprite" "64x64.aseprite" "128x128.aseprite")

# Prompt the user to select a template.
echo "Available Aseprite templates:"
for i in "${!ASEPRITE_TEMPLATES[@]}"; do
  echo "$((i+1))) ${ASEPRITE_TEMPLATES[i]}"
done
read -p "Select a template (1-5): " TEMPLATE_NUM

# Validate user input for template selection.
if [ "$TEMPLATE_NUM" -lt 1 ] || [ "$TEMPLATE_NUM" -gt 5 ]; then
  echo "Invalid selection. Please run the script again and select a number between 1 and 5."
  exit 1
fi

# Adjust index to match array and determine the selected template.
TEMPLATE_INDEX=$((TEMPLATE_NUM-1))
ASEPRITE_TEMPLATE=${ASEPRITE_TEMPLATES[$TEMPLATE_INDEX]}
PIXEL_DIMENSION="${ASEPRITE_TEMPLATE%.*}"  # Extracts dimension like '8x8' from the filename.

# Prompt for the starting and ending ID numbers.
read -p "Enter the starting ID number: " START_NUM
read -p "Enter the ending ID number: " END_NUM

# Validate user input for ID numbers.
if ! [[ "$START_NUM" =~ ^[0-9]+$ ]] || ! [[ "$END_NUM" =~ ^[0-9]+$ ]] || [ "$START_NUM" -ge "$END_NUM" ]; then
  echo "Invalid input. Starting ID should be a number, less than the ending ID number."
  exit 1
fi

# Ensure the destination directories exist.
mkdir -p "$DEST_JSON_DIR"
mkdir -p "$DEST_ASEPRITE_DIR"

# Loop through the range and create copies with updated names.
for i in $(seq $START_NUM $END_NUM); do
    # Copy and rename the metadata JSON file.
    JSON_FILE="$DEST_JSON_DIR/$i.json"
    cp "$METADATA_DIR/standard_template.json" "$JSON_FILE"

    # Update the "name" and "pixels" field in the JSON file.
    jq --arg name "Proto Tower $i" --arg pixels "$PIXEL_DIMENSION" \
       '.name = $name | .attributes[0].value = $pixels' \
       "$JSON_FILE" > temp.json && mv temp.json "$JSON_FILE"

    # Copy and rename the Aseprite file based on the selected template.
    ASEPRITE_FILE="$DEST_ASEPRITE_DIR/$i.aseprite"
    cp "$ASEPRITE_DIR/$ASEPRITE_TEMPLATE" "$ASEPRITE_FILE"
done

echo "Standard deployment setup complete for IDs $START_NUM to $END_NUM using $ASEPRITE_TEMPLATE."
