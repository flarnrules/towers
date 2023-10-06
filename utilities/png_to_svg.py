import imageio
import os

# Set the path and base filename
PATH = "../media/test_images/"
BASE_FILENAME = "a_tower"  # Without extension

def png_to_svg(input_path, output_path):
    # Convert PNG to BMP because potrace requires it
    bmp_path = input_path.replace('.png', '.bmp')
    image = imageio.imread(input_path)
    imageio.imwrite(bmp_path, image)

    # Call potrace to convert BMP to SVG
    os.system(f"potrace {bmp_path} -s -o {output_path}")

    # Optionally, delete BMP file
    os.remove(bmp_path)

if __name__ == "__main__":
    input_file = PATH + BASE_FILENAME + ".png"
    output_file = PATH + BASE_FILENAME + ".svg"

    png_to_svg(input_file, output_file)
    print(f"Image converted and saved as {output_file}!")