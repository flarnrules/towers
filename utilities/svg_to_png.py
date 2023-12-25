import cairosvg

def svg_to_png(svg_file, png_file):
    try:
        cairosvg.svg2png(url=svg_file, write_to=png_file)
        print(f"Conversion successful. PNG file saved as: {png_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
svg_file = '/mnt/c/users/benjamin/documents/calis_family_farm/calisfamilyfarmlogo.svg'  # Replace with your SVG file path
png_file = '/mnt/c/users/benjamin/documents/calis_family_farm/calisfamilyfarm.png'  # Replace with your desired output PNG file path

svg_to_png(svg_file, png_file)
