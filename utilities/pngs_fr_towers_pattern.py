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

    # Load the image in color
    image_color = cv2.imread(input_path)
    
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
        # Bounding box of the contour
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

        # Convert the extracted image to square with transparency
        size = max(w, h)
        canvas = np.zeros((size, size, 4), dtype=np.uint8)
        start_x = (size - w) // 2
        start_y = (size - h) // 2
        canvas[start_y:start_y+h, start_x:start_x+w, :3] = tower_img
        canvas[start_y:start_y+h, start_x:start_x+w, 3] = mask

        # Save the extracted tower
        tower_output_path = os.path.join(towers_output_folder, f'tower_{idx}.png')
        cv2.imwrite(tower_output_path, canvas)

        # For debugging: Draw contour and index on the debug_image
        color = tuple(np.random.randint(0, 255, 3).tolist())  # BGR format. Random color for each contour
        index_number_color = (0, 0, 0) # Blue in BGR format.
        middle_index_color = (250, 250, 250)
        print(color)
        cv2.drawContours(debug_image, [contour], -1, color, 2)
        cv2.putText(debug_image, str(idx), (x + 5, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, index_number_color, 2)
        print("the index number color is ", index_number_color)

    # Save the debug image
    cv2.imwrite(debug_output_path, debug_image)
    print(f"Extracted {len(contours)} towers and generated a debug image!")

# Update paths accordingly
input_path = '../media/raw_formatted/2.png'
towers_output_folder = '../media/test_2.png'
debug_output_path = '../media/debug_2.png'

extract_and_debug_towers(input_path, towers_output_folder, debug_output_path)
