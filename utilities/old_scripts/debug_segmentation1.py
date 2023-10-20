import cv2
import numpy as np
import os

def debug_towers_segmentation(input_path, debug_output_path):
    # Load the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Convert to color for debugging

    # Threshold the image to binary using Otsu's method
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Refine binary image
    kernel = np.ones((1,1),np.uint8)
    eroded = cv2.erode(binary, kernel, iterations = 1)
    refined_binary = cv2.dilate(eroded, kernel, iterations = 1)

    # Find contours on the refined binary image
    contours, _ = cv2.findContours(refined_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    min_area = 150
    contours = [c for c in contours if cv2.contourArea(c) > min_area]

    # For each contour, draw it on the color_image
    for idx, contour in enumerate(contours):
        color = tuple(np.random.randint(0, 255, 3).tolist())  # Random color for each contour
        cv2.drawContours(color_image, [contour], -1, color, 2)

        # Get the center of the contour to place the text
        M = cv2.moments(contour)
        if M["m00"] != 0:  # Check to avoid division by zero
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        # Place the index on the tower
        cv2.putText(color_image, str(idx), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    # Save the debug image
    cv2.imwrite(debug_output_path, color_image)
    print("Debug image generated!")

# Update paths accordingly
input_path = '../media/concept_art/towers_pattern_manual_preprocess.png'
debug_output_path = '../media/debug_images/debug_segmentation5.png'

debug_towers_segmentation(input_path, debug_output_path)
