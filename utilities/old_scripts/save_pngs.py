import cv2
import numpy as np
import os

def save_towers_as_png(input_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the original image in grayscale and also in color for transparent background creation
    image_gray = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    image_color = cv2.imread(input_path)

    # Threshold the image to binary using Otsu's method
    _, binary = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for idx, contour in enumerate(contours):
        # Extract bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Make the bounding box square
        if w > h:
            diff = w - h
            y -= diff // 2
            h = w
            if y < 0:  # Ensure the bounding box doesn't exceed image boundaries
                y = 0
        else:
            diff = h - w
            x -= diff // 2
            w = h
            if x < 0:  # Ensure the bounding box doesn't exceed image boundaries
                x = 0

        # Extract tower from the color image
        tower_img = image_color[y:y+h, x:x+w]

        # Create a mask for transparency
        mask = binary[y:y+h, x:x+w]
        tower_img = cv2.merge([tower_img[:,:,0], tower_img[:,:,1], tower_img[:,:,2], mask])

        # Save as PNG
        tower_path = os.path.join(output_dir, f'tower_{idx}.png')
        cv2.imwrite(tower_path, tower_img)
        print(f"Saved {tower_path}")

    print("All towers saved!")

# Update paths accordingly
input_path = '../media/concept_art/towers_pattern_manual_preprocess.png'
output_dir = '../media/test_images/towers_png'

save_towers_as_png(input_path, output_dir)
