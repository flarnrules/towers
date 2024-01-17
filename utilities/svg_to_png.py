import cairosvg

def svg_to_png(svg_file, png_file):
    try:
        cairosvg.svg2png(url=svg_file, write_to=png_file)
        print(f"Conversion successful. PNG file saved as: {png_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
svg_file = '../collections/2-proto_towers/images/273/273.svg'  # Replace with your SVG file path
png_file = '../collections/2-proto_towers/images/273/273.png'  # Replace with your desired output PNG file path

svg_to_png(svg_file, png_file)
