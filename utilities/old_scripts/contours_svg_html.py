import cv2
import numpy as np
import os
from png_to_svg import png_to_svg

def segment_and_convert(input_path, output_dir):
    # Load the image in grayscale
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Threshold the image to binary using Otsu's method
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    min_area = 50
    contours = [c for c in contours if cv2.contourArea(c) > min_area]

    # Create an HTML file to store inline SVGs
    html_content = "<html><body>"

    # Segment, convert to SVG, and append to HTML content
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

        # Temp PNG output path
        temp_png_path = os.path.join(output_dir, f"tower_{idx + 1}.png")
        cv2.imwrite(temp_png_path, output_image)
        
        # SVG output path
        svg_path = os.path.join(output_dir, f"tower_{idx + 1}.svg")
        
        # Convert PNG to SVG
        png_to_svg(temp_png_path, svg_path)
        
        # Delete the temporary PNG
        os.remove(temp_png_path)

        # Append SVG content to HTML
        with open(svg_path, 'r') as svg_file:
            svg_content = svg_file.read()
        html_content += svg_content
        os.remove(svg_path)

    # Close the HTML tags
    html_content += "</body></html>"

    # Save the HTML content to a file
    with open(os.path.join(output_dir, "towers_combined.html"), 'w') as html_file:
        html_file.write(html_content)

    print("SVG conversion and HTML generation completed!")

# Update paths accordingly
input_path = '../media/concept_art/towers_pattern_manual_preprocess.png'
output_dir = '../media/test_images/'

segment_and_convert(input_path, output_dir)
