from utilities.png_to_svg_bw import png_to_svg_invert  # Import your function
import os

# Input and output directories
input_dir = "../media/wip/300/batch"
output_dir = "../media/wip/300/svg"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".png"):
        png_path = os.path.join(input_dir, filename)
        svg_filename = filename.replace(".png", ".svg")
        svg_path = os.path.join(output_dir, svg_filename)
        
        # Perform the conversion
        png_to_svg_invert(png_path, svg_path)
