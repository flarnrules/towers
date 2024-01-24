import cv2

def create_svg_from_png(image_path, svg_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape

    # Start the SVG file with a default background (optional)
    svg_output = '<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(width, height)
    svg_output += '<rect width="100%" height="100%" fill="#FFFFFF"/>\n'  # White background

    # Function to check if a pixel is black
    def is_black(value):
        return value < 128  # Threshold for black

    # Function to create rectangles for contiguous black pixels
    def create_rectangles(image):
        rectangles = []
        visited = set()

        def expand_rectangle(x, y):
            if (x, y) in visited or not is_black(image[y, x]):
                return 0, 0
            visited.add((x, y))
            width, height = expand_rectangle(x + 1, y)
            return width + 1, height

        for y in range(height):
            x = 0
            while x < width:
                if is_black(image[y, x]) and (x, y) not in visited:
                    rect_width, rect_height = expand_rectangle(x, y)
                    rectangles.append((x, y, rect_width, rect_height))
                    x += rect_width
                else:
                    x += 1
        return rectangles

    rectangles = create_rectangles(image)
    for x, y, rect_width, rect_height in rectangles:
        svg_output += f'<rect x="{x}" y="{y}" width="{rect_width}" height="{rect_height}" fill="#000000"/>\n'

    # End the SVG file
    svg_output += '</svg>'

    # Write to SVG file
    with open(svg_path, 'w') as file:
        file.write(svg_output)

# Usage
create_svg_from_png('media/wip/300/reallycool.png', 'media/wip/300/reallycool.svg')
