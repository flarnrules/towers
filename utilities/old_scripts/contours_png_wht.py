import cv2
import numpy as np
import os

# Directory paths
input_dir = '../media/concept_art/'
output_dir = '../media/test_images/'

# Input image variables
image_name = 'towers_pattern'  # Change this to the desired image name without extension
image_extension = '.png'  # Change this to the desired extension e.g., '.jpg', '.png'

# Construct full input path
input_path = os.path.join(input_dir, image_name + image_extension)

# Load the image in grayscale
image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

# Threshold the image to binary using Otsu's method
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (optional)
min_area = 50
contours = [c for c in contours if cv2.contourArea(c) > min_area]

# Output each contour as an individual image
for idx, contour in enumerate(contours):
    mask = np.zeros_like(binary)
    cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
    
    # Create a white background image of the same size
    white_background = 255 * np.ones_like(image)
    
    # Combine the segmented tower with the white background
    output_image = cv2.bitwise_and(image, image, mask=mask)
    inverse_mask = cv2.bitwise_not(mask)
    white_part = cv2.bitwise_and(white_background, white_background, mask=inverse_mask)
    output_image = cv2.bitwise_or(output_image, white_part)
    
    # Construct output path
    output_path = os.path.join(output_dir, f"{image_name}_{idx + 1}.png")
    cv2.imwrite(output_path, output_image)
