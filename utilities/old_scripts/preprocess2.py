import cv2
import numpy as np

def preprocess_image(input_path, output_path):
    # Load the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Binarize the image using Otsu's method
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Erode the image slightly to separate touching towers
    kernel = np.ones((3, 3), np.uint8)
    eroded = cv2.erode(binary, kernel, iterations=1)

    # Invert the image back to original form
    output_image = cv2.bitwise_not(eroded)

    # Save the preprocessed image
    cv2.imwrite(output_path, output_image)

    print(f"Preprocessed image saved to {output_path}")

input_path = '../media/concept_art/towers_pattern.png'
output_path = '../media/test_images/preprocessed_towers.png'

preprocess_image(input_path, output_path)
