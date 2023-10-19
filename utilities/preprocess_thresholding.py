import cv2
import numpy as np

# Load the image
image_path = "../media/concept_art/towers_pattern.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Threshold the image
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

towers = []
for contour in contours:
    # Get bounding box for each tower
    x, y, w, h = cv2.boundingRect(contour)
    tower = thresholded[y:y+h, x:x+w]
    towers.append(tower)

# Rearrange towers randomly
# np.random.shuffle(towers)

# Create a new blank canvas
height, width = image.shape
canvas = np.ones((height, width), dtype=np.uint8) * 255

# Place the shuffled towers on the canvas
x_offset = 0
for tower in towers:
    tower_width = tower.shape[1]
    
    # Ensure you're not exceeding the canvas width
    if x_offset + tower_width > width:
        break

    canvas[:tower.shape[0], x_offset:x_offset + tower_width] = tower
    
    # Increment the x_offset by the tower's width (and optionally add some spacing between towers)
    x_offset += tower_width + 5  # 5 pixels of spacing for example

cv2.imwrite("output_image.jpg", canvas)
