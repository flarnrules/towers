from PIL import Image

def invert_colors(image_path, output_path):
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Invert the colors
            inverted_img = Image.eval(img, lambda x: 255 - x)

            # Save the inverted image
            inverted_img.save(output_path)
            print(f"Inverted image saved as: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
image_path = '/mnt/c/users/benjamin/documents/calis_family_farm/calisfamilyfarm.png'  # Replace with your image file path
output_path = '/mnt/c/users/benjamin/documents/calis_family_farm/calisfamilyfarminverted.png'  # Replace with your desired output file path

invert_colors(image_path, output_path)
