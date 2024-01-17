import cv2

def create_svg_from_png(image_path, svg_path, background_color=(255, 255, 255)):
    # Load the image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Start the SVG file with the background color
    svg_output = '<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">\n'
    bg_hex_color = f'#{background_color[2]:02x}{background_color[1]:02x}{background_color[0]:02x}'
    svg_output += f'<rect width="100%" height="100%" fill="{bg_hex_color}"/>\n'

    # Function to convert color to hex
    def color_to_hex(color):
        return f'#{color[2]:02x}{color[1]:02x}{color[0]:02x}'

    # Iterate over each row
    for y in range(height):
        start_x = None
        current_color = None
        for x in range(width):
            pixel_color = image[y, x]
            if start_x is None or not all(pixel_color == current_color):
                if start_x is not None and not all(current_color == background_color):
                    # End of a segment, write a rectangle if not background color
                    hex_color = color_to_hex(current_color)
                    rect_width = ((x - start_x) / width) * 100
                    svg_output += f'<rect x="{(start_x / width) * 100}%" y="{(y / height) * 100}%" width="{rect_width}%" height="1%" fill="{hex_color}"/>\n'
                start_x = x
                current_color = pixel_color
        # Check for the last segment in a row
        if start_x is not None and not all(current_color == background_color):
            hex_color = color_to_hex(current_color)
            rect_width = ((width - start_x) / width) * 100
            svg_output += f'<rect x="{(start_x / width) * 100}%" y="{(y / height) * 100}%" width="{rect_width}%" height="1%" fill="{hex_color}"/>\n'

    # End the SVG file
    svg_output += '</svg>'

    # Write to SVG file
    with open(svg_path, 'w') as file:
        file.write(svg_output)

# Usage
create_svg_from_png('media/wip/276/276.png', 'media/wip/276/276.svg')
