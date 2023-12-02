import os
import shutil

def copy_and_rename_images(source_dir, target_dir='originals'):
    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Get all .png files in the source directory
    files = [f for f in os.listdir(source_dir) if f.endswith('.png')]

    # Copy and rename files
    for i, file in enumerate(files, start=1):
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(target_dir, f"{i}.png")
        shutil.copy2(source_file, target_file)
        print(f"Copied and renamed {file} to {target_file}")

# Usage
source_directory = "originals" # Replace with your source directory path
copy_and_rename_images(source_directory)
