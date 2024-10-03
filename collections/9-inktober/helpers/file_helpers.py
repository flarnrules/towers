import os
import json
from datetime import datetime

def get_next_id(folder):
    # List all files in the folder that end with '.png'
    existing_files = [f for f in os.listdir(folder) if f.endswith('.png')]
    
    # Extract numeric IDs from file names (e.g., '1.png' -> 1, '2.png' -> 2)
    existing_ids = [int(f.split('.')[0]) for f in existing_files if f.split('.')[0].isdigit()]
    
    # If there are no existing IDs, return 1
    if not existing_ids:
        return 1
    else:
        # Find the smallest missing ID
        return min(set(range(1, max(existing_ids) + 2)) - set(existing_ids))

# Function to generate the next PNG and JSON file names
def get_file_names(image_folder, metadata_folder):
    next_id = get_next_id(image_folder)
    image_file = f"{next_id}.png"
    json_file = f"{next_id}.json"
    return os.path.join(image_folder, image_file), os.path.join(metadata_folder, json_file)

# Function to generate and save the JSON metadata using a template
def save_json_metadata(json_file_path, prompt_name, pixels, dimensions, artist, iteration):
    metadata_template = {
        "name": prompt_name,
        "description": "This is Inktober, a growable collection of digital drawings that follows most of the rules and prompts of Inktober. \n \n 1) Make a drawing in ink \n 2) Post it \n 3) Hashtag it with #inktober and #inktober<year> \n 4) Repeat ",
        "attributes": [
            {
                "trait_type": "pixels",
                "value": pixels
            },
            {
                "trait_type": "dimensions",
                "value": dimensions
            },
            {
                "trait_type": "year",
                "value": datetime.now().year
            },
            {
                "trait_type": "day",
                "value": datetime.now().day
            },
            {
                "trait_type": "artist",
                "value": artist,
            },
            {
                "trait_type": "iteration",
                "value": iteration,
            }
        ]
    }

    with open(json_file_path, 'w') as json_file:
        json.dump(metadata_template, json_file, indent=4)


def calculate_iteration(metadata_folder, prompt_value, artist):
    """Calculate the iteration based on other JSON files with the same prompt and artist."""
    iteration_count = 1  # Start with 1 if no matches found
    for file_name in os.listdir(metadata_folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(metadata_folder, file_name)
            with open(file_path, 'r') as json_file:
                metadata = json.load(json_file)
                # Check if prompt and artist match
                if metadata["name"] == prompt_value and metadata["attributes"]:
                    for attr in metadata["attributes"]:
                        if attr["trait_type"] == "artist" and attr["value"] == artist:
                            iteration_count += 1
    return iteration_count
