from PIL import Image
import subprocess

def convert_to_bmp(input_image, output_bmp):
    with Image.open(input_image) as image:
        # Convert image to RGB or RGBA mode before saving as BMP
        if image.mode == 'LA':
            # If you need to preserve transparency, convert to 'RGBA'
            image = image.convert('RGBA')
        elif image.mode != 'RGB':
            # Convert non-RGB images to grayscale ('L') or you can choose to convert to 'RGB'
            image = image.convert('RGB')
        image.save(output_bmp, "BMP")

def convert_to_svg(input_bmp, output_svg):
    try:
        subprocess.run(["potrace", input_bmp, "-s", "-o", output_svg], check=True)
        print(f"SVG file created: {output_svg}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Usage
input_image = "media/wip/305/305.png"  # Replace with your image path
output_bmp = "media/wip/305/305.bmp"   # Temporary BMP file
output_svg = "media/wip/305/305.svg" # Final SVG file

convert_to_bmp(input_image, output_bmp)
convert_to_svg(output_bmp, output_svg)