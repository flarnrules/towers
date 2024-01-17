import cv2
import numpy as np

# Load the image
image = cv2.imread('path/to/your/image.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the edges in the image using canny detector
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Initialize SVG output
svg_header = f'<svg width="{image.shape[1]}" height="{image.shape[0]}" xmlns="http://www.w3.org/2000/svg">\n'
svg_content = ""
svg_footer = '</svg>'

# Draw the contours
for cnt in contours:
    # Create a string with the contour points in SVG path format
    svg_path = 'M' + ' L'.join([f'{int(x)},{int(y)}' for x, y in cnt[:, 0]]) + ' Z\n'
    svg_content += f'<path d="{svg_path}" stroke="black" fill="none"/>\n'

# Save to SVG file
with open('output.svg', 'w') as f:
    f.write(svg_header + svg_content + svg_footer)
