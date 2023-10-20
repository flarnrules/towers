import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('../media/concept_art/towers_pattern.png', cv2.IMREAD_GRAYSCALE)

# Threshold the image to binary using Otsu's method
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (optional)
min_area = 50
contours = [c for c in contours if cv2.contourArea(c) > min_area]

# Visualize the contours (for debugging purposes)
debug_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(debug_image, contours, -1, (0,255,0), 2)
cv2.imwrite('contours.png', debug_image)
