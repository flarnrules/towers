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
        
        <!-- Left Tower: Outer Shape -->
        <path d="M 100 350 Q 120 200 130 100 Q 120 50 110 0" fill="none" stroke="#000" stroke-width="4"/>

        <!-- Left Tower: First Inner Line -->
        <path d="M 115 350 Q 130 220 138 110" fill="none" stroke="#000" stroke-width="2"/>

        <!-- Left Tower: Second Inner Line -->
        <path d="M 130 350 Q 142 220 148 120" fill="none" stroke="#000" stroke-width="2"/>
        
        <!-- Right Tower: Outer Shape -->
        <path d="M 270 350 Q 250 200 240 100 Q 250 50 260 0" fill="none" stroke="#000" stroke-width="4"/>

        <!-- Right Tower: First Inner Line -->
        <path d="M 255 350 Q 240 220 232 110" fill="none" stroke="#000" stroke-width="2"/>

        <!-- Right Tower: Second Inner Line -->
        <path d="M 240 350 Q 228 220 222 120" fill="none" stroke="#000" stroke-width="2"/>
        
        <!-- Base details -->
        <path d="M 90 350 L 170 350 Q 160 340 150 330 Q 140 320 130 320 Q 120 320 110 330 Z" fill="none" stroke="#000" stroke-width="3"/>
        <path d="M 230 350 L 310 350 Q 300 340 290 330 Q 280 320 270 320 Q 260 320 250 330 Z" fill="none" stroke="#000" stroke-width="3"/>
        <path d="M 170 350 L 230 350" fill="none" stroke="#000" stroke-width="3"/>
        <path d="M 100 350 L 60 360 L 40 370" fill="none" stroke="#000" stroke-width="3"/>
        <path d="M 300 350 L 340 360 L 360 370" fill="none" stroke="#000" stroke-width="3"/>

    </svg>

    """

    # Convert the SVG string to PNG
    svg_to_png(svg_string, "output_image.png")
    print("SVG has been converted to output_image.png!")
