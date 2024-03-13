import os
import shutil

# Configuration
SOURCE_FOLDER = '../aseprite/not_yet_created'
DESTINATION_FOLDER = '../asprite/'
NEW_PREFIX = 'ASTEROID_TOWER_'
NEW_EXTENSION = '.aseprite'

# Ensure destination folder exists
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

# Process files
for filename in os.listdir(SOURCE_FOLDER):
    # Construct new filename
    original_name, original_extension = os.path.splitext(filename)
    new_name = f"{NEW_PREFIX}{original_name}{NEW_EXTENSION}"
    
    # Copy and rename files
    src_path = os.path.join(SOURCE_FOLDER, filename)
    dest_path = os.path.join(DESTINATION_FOLDER, new_name)
    shutil.copy(src_path, dest_path)
    print(f"Copied and renamed {filename} to {new_name}")

print("Process completed successfully.")
