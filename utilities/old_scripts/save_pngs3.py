import cv2
import numpy as np
import os

def save_towers_as_png(input_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

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

        # Within the bounding box, find contours again to filter out artifacts
        roi = binary[y:y+h, x:x+w]
        sub_contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        areas = [cv2.contourArea(c) for c in sub_contours]
        max_index = np.argmax(areas)  # Index of the main tower

        # Create a mask using only the main tower contour
        mask = np.zeros_like(roi)
        cv2.drawContours(mask, sub_contours, max_index, (255), thickness=cv2.FILLED)

        # Extract tower with mask applied
        tower_img = cv2.bitwise_and(image_color[y:y+h, x:x+w], image_color[y:y+h, x:x+w], mask=mask)
        
        # Convert the extracted image to square
        size = max(w, h)
        canvas = np.zeros((size, size, 4), dtype=np.uint8)
        start_x = (size - w) // 2
        start_y = (size - h) // 2
        canvas[start_y:start_y+h, start_x:start_x+w, :3] = tower_img
        canvas[start_y:start_y+h, start_x:start_x+w, 3] = mask

        # Save as PNG
        tower_path = os.path.join(output_dir, f'tower_{idx}.png')
        cv2.imwrite(tower_path, canvas)
        print(f"Saved {tower_path}")

    print("All towers saved!")

# Update paths accordingly
input_path = '../media/concept_art/towers_pattern_manual_preprocess.png'
output_dir = '../media/test_images/towers_png3'

save_towers_as_png(input_path, output_dir)
