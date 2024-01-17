import base64

# Load the image and convert it to base64
with open("path/to/your/image.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Create an SVG image string
svg_image = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">
    <image width="100%" height="100%" xlink:href="data:image/png;base64,{encoded_string}"/>
</svg>
"""

# Write the SVG file
with open("image.svg", "w") as svg_file:
    svg_file.write(svg_image)
