import cv2
import numpy as np
import os

def extract_and_debug_towers(input_path, towers_output_folder, debug_output_path):
    # Ensure the output directory exists
    if not os.path.exists(towers_output_folder):
        os.makedirs(towers_output_folder)
    
    # Load the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    debug_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color for debugging

    # Threshold the image to binary using Otsu's method
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Refine binary image
    kernel = np.ones((1,1), np.uint8)
    eroded = cv2.erode(binary, kernel, iterations=1)
    refined_binary = cv2.dilate(eroded, kernel, iterations=1)

    # Find contours on the refined binary image
    contours, _ = cv2.findContours(refined_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    min_area = 150
    contours = [c for c in contours if cv2.contourArea(c) > min_area]

    # For each contour, extract tower and debug
    for idx, contour in enumerate(contours):
        # Extract tower from the grayscale image
        x, y, w, h = cv2.boundingRect(contour)
        tower = image[y:y+h, x:x+w]

        # Make sure only the largest blob (tower) is retained
        tower_binary = tower.copy()
        tower_contours, _ = cv2.findContours(tower_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        tower_contours = sorted(tower_contours, key=cv2.contourArea, reverse=True)  # Sort contours by area, largest first
        mask = np.zeros_like(tower_binary)
        cv2.drawContours(mask, [tower_contours[0]], -1, 255, thickness=cv2.FILLED)  # Fill largest contour
        tower = cv2.bitwise_and(tower, mask)

        # Make the background transparent
        _, alpha = cv2.threshold(tower, 0, 255, cv2.THRESH_BINARY)
        b, g, r = cv2.split(debug_image[y:y+h, x:x+w])
        rgba = [r, g, b, alpha]
        dst = cv2.merge(rgba, 4)

        # Save the tower image
        tower_output_path = os.path.join(towers_output_folder, f"tower_{idx}.png")
        cv2.imwrite(tower_output_path, dst)
        
        # For debugging: Draw contour and index on the debug_image
        color = tuple(np.random.randint(0, 255, 3).tolist())  # Random color for each contour
        cv2.drawContours(debug_image, [contour], -1, color, 2)
        cv2.putText(debug_image, str(idx), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Save the debug image
    cv2.imwrite(debug_output_path, debug_image)
    print(f"Extracted {len(contours)} towers and generated a debug image!")

# Update paths accordingly
input_path = '../media/concept_art/towers_pattern_manual_preprocess.png'
towers_output_folder = '../media/test_images/towers_png4'
debug_output_path = '../media/debug_images/debug_segmentation_with_indices.png'

extract_and_debug_towers(input_path, towers_output_folder, debug_output_path)
