from PIL import Image

# Set the path and base filename
PATH = "../media/test_images/"
BASE_FILENAME = "a_tower"  # Without extension

def convert_jpg_to_png(input_path, output_path):
    """Convert a JPG image to PNG format."""
    with Image.open(input_path) as img:
        img.save(output_path, "PNG")

if __name__ == "__main__":
    input_file = PATH + BASE_FILENAME + ".jpg"
    output_file = PATH + BASE_FILENAME + ".png"

    convert_jpg_to_png(input_file, output_file)
    print(f"Image converted and saved as {output_file}!")
