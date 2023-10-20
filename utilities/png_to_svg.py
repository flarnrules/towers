import cv2
import imageio
import os

# Set the path and base filename
PATH = "../media/test_images/"
BASE_FILENAME = "6_1_rotate_better_512"  # Without extension

def preprocess_image(image_path, save_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply Otsu's thresholding to convert to black and white
    _, bw_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Apply Canny edge detection
    edges = cv2.Canny(bw_image, 150, 350)
    
    # Save the edge-detected image
    cv2.imwrite(save_path, edges)

def png_to_svg(input_path, output_path):
    # Convert PNG to BMP because potrace requires it
    bmp_path = input_path.replace('.png', '.bmp')
    image = imageio.imread(input_path)
    imageio.imwrite(bmp_path, image)

    # Call potrace to convert BMP to SVG
    os.system(f"potrace {bmp_path} -s -o {output_path}")

    # Optionally, delete BMP file
    os.remove(bmp_path)

def png_to_svg_invert(input_path, output_path):
    # Preprocess the PNG image
    processed_path = input_path.replace('.png', '_processed.png')
    preprocess_image(input_path, processed_path)
    
    # Convert PNG to BMP because potrace requires it
    bmp_path = processed_path.replace('.png', '.bmp')
    image = imageio.imread(processed_path)
    imageio.imwrite(bmp_path, image)

    # Call potrace to convert BMP to SVG
    os.system(f"potrace {bmp_path} --invert -s -o {output_path}")

    # Optionally, delete BMP file
    os.remove(bmp_path)


if __name__ == "__main__":
    input_file = PATH + BASE_FILENAME + ".png"
    output_file = PATH + BASE_FILENAME + ".svg"

    png_to_svg(input_file, output_file)
    print(f"Image converted and saved as {output_file}!")