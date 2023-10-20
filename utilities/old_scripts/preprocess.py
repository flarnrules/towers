import cv2
import numpy as np

def preprocess(input_path, output_path=None):
    """
    Preprocess the image to convert it to a binary black & white image with sharp lines.

    :param input_path: path to the input image
    :param output_path: optional path to save the preprocessed image
    :return: preprocessed image
    """

    # 1. Load the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Threshold the image to binary using Otsu's method
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. Sharpen the binary image
    sharpening_filter = np.array([[-1, -1, -1], 
                                  [-1,  9, -1], 
                                  [-1, -1, -1]])
    sharpened = cv2.filter2D(binary, -1, sharpening_filter)

    # 4. Separate touching towers

    if output_path:
        cv2.imwrite(output_path, sharpened)

    return sharpened

if __name__ == "__main__":
    preprocess('../media/concept_art/towers_pattern.png', '../media/test_images/towers_pattern_preprocessed.png')
