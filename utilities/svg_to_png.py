import cairosvg

def svg_to_png(svg_string, output_file):
    # Convert SVG string to PNG and save to output_file
    cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), write_to=output_file)

if __name__ == "__main__":
    # Your SVG string goes here
    svg_string = """
    <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
        <!-- Background -->
        <rect width="100%" height="100%" fill="#f5e6c8"/>

        <!-- Left Tower: Base to first curve -->
        <path d="M 95 350 Q 105 325 115 290" fill="none" stroke="#000" stroke-width="8"/>
        
        <!-- Left Tower: First curve to the top -->
        <path d="M 115 290 Q 125 260 120 200" fill="none" stroke="#000" stroke-width="8"/>

        <!-- Left Tower: Top edge -->
        <path d="M 120 200 Q 110 175 95 150" fill="none" stroke="#000" stroke-width="8"/>

        <!-- Left Tower: Downwards edge -->
        <path d="M 95 150 L 100 350" fill="none" stroke="#000" stroke-width="8"/>
        
        <!-- Right Tower: Base to first curve -->
        <path d="M 235 350 Q 245 325 255 290" fill="none" stroke="#000" stroke-width="8"/>
        
        <!-- Right Tower: First curve to the top -->
        <path d="M 255 290 Q 265 260 260 200" fill="none" stroke="#000" stroke-width="8"/>

        <!-- Right Tower: Top edge -->
        <path d="M 260 200 Q 250 175 235 150" fill="none" stroke="#000" stroke-width="8"/>

        <!-- Right Tower: Downwards edge -->
        <path d="M 235 150 L 240 350" fill="none" stroke="#000" stroke-width="8"/>
        
    </svg>
    """

    # Convert the SVG string to PNG
    svg_to_png(svg_string, "output_image.png")
    print("SVG has been converted to output_image.png!")
