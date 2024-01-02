from PIL import Image
import os

def resize_image(input_path, output_path, new_width, new_height):
    with Image.open(input_path) as img:
        print(f"Original dimensions: {img.size}")
        resized_img = img.resize((new_width, new_height), Image.NEAREST)
        resized_img.save(output_path)
        print(f"New dimensions: {resized_img.size}")


def bulk_resize(folder_path, new_width, new_height):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_file = os.path.join(folder_path, filename)
            output_file = os.path.join(folder_path, f"resized_{filename}")

            resize_image(input_file, output_file, new_width, new_height)
            print(f"Resized '{input_file}' and saved to '{output_file}'")


resize_image('../collections/2-proto_towers/media/gifs/90.gif', '../collections/2-proto_towers/images/51-100/90.gif', 768, 768)
# bulk_resize('../collections/2-proto_towers/bulkresize', 768, 768)