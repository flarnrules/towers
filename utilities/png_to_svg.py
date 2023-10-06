import numpy as np
from PIL import Image
import potrace

def image_to_svg(input_path, output_path):
    # Load the image
    image = Image.open(input_path)
    
    # Convert to grayscale
    grayscale_image = image.convert("L")
    
    # Binarize the image
    threshold = 128
    binary_image = grayscale_image.point(lambda p: p > threshold and 255)
    bitmap = potrace.Bitmap(np.array(binary_image))
    
    # Trace the image to generate paths
    path = bitmap.trace()
    
    # Generate SVG data
    with open(output_path, "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.0" width="{}" height="{}">\n'.format(image.width, image.height))
        for curve in path.to_curves():
            f.write('  <path d="')
            for segment in curve:
                if segment.is_corner():
                    pt = segment.c
                    f.write("L {} {} ".format(pt.x, pt.y))
                else:
                    c1, c2, pt = segment.c1, segment.c2, segment.e
                    f.write("C {} {}, {} {}, {} {} ".format(c1.x, c1.y, c2.x, c2.y, pt.x, pt.y))
            f.write('Z"/>\n')
        f.write('</svg>')

# Usage
image_to_svg("../media/test_images/a_tower.png", "a_tower.svg")