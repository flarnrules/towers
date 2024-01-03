from PIL import Image
import os
import re

# Parameters
input_folder = '../collections/2-proto_towers/media/original_pngs/101-150'
output_folder = '../collections/2-proto_towers/images/51-100'
new_width = 768
new_height = 768

def resize_image(input_path, output_path, new_width, new_height):
    with Image.open(input_path) as img:
        print(f"Original dimensions: {img.size}")
        resized_img = img.resize((new_width, new_height), Image.NEAREST)

        # Extracting the number from the filename
        base_name = os.path.basename(input_path)
        number = re.search(r'\d+', base_name)
        if number:
            new_filename = f"{number.group(0)}.png"  # Assumes the output is always PNG
        else:
            new_filename = base_name

        new_output_path = os.path.join(output_path, new_filename)
        resized_img.save(new_output_path)
        print(f"New dimensions: {resized_img.size}, saved to {new_output_path}")

def bulk_resize(input_folder, output_folder, new_width, new_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_file = os.path.join(input_folder, filename)
            resize_image(input_file, output_folder, new_width, new_height)

# Run the script
bulk_resize(input_folder, output_folder, new_width, new_height)
