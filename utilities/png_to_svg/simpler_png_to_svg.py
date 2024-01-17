import cv2

# Read the image
image = cv2.imread('path/to/your/100x100image.png')

# Begin the SVG file
svg_output = '<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">\n'

# Iterate over each pixel and create a rectangle in the SVG for each one
for y in range(100):
    for x in range(100):
        # Get the color of the pixel
        b, g, r = image[y, x]
        # Convert the color to hex format
        hex_color = f'#{r:02x}{g:02x}{b:02x}'
        # Create an SVG rectangle for the current pixel
        svg_output += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{hex_color}" />\n'

# End the SVG file
svg_output += '</svg>'

# Write the SVG data to a file
with open('output.svg', 'w') as file:
    file.write(svg_output)
