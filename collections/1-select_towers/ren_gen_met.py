## This script renames and generates metadata for the files renamed
## And saved in the images folder
## If needed it should create a metadata folder

import os
import shutil
import json

source_directory = "originals"  # Replace with your source directory path
images_directory = "images"
metadata_directory = "metadata"

def create_metadata_and_images(source_dir, img_dir=images_directory, meta_dir=metadata_directory):
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the images and metadata directories if they don't exist
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    if not os.path.exists(meta_dir):
        os.makedirs(meta_dir)

    # Get and sort all .png files in the source directory
    files = sorted([f for f in os.listdir(source_dir) if f.endswith('.png')])

    # Copy and rename files, and create corresponding JSON files in metadata directory
    for i, file in enumerate(files, start=1):
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(img_dir, f"{i}.png")
        json_file = os.path.join(meta_dir, f"{i}.json")

        # Copy the image file
        shutil.copy2(source_file, target_file)
        print(f"Copied and renamed {file} to {target_file}")

        # Create a corresponding JSON file in the metadata directory
        with open(json_file, 'w') as jf:
            json.dump([], jf)  # Use {} for an empty dictionary if preferred
        print(f"Created JSON file {json_file}")

create_metadata_and_images(source_directory)
