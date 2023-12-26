from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    # Open the image file
    with Image.open(input_path) as img:
        # Print original dimensions
        print(f"Original dimensions: {img.size}")

        # Resize the image with nearest-neighbor algorithm
        resized_img = img.resize((new_width, new_height), Image.NEAREST)

        # Save the resized image
        resized_img.save(output_path)

        # Print new dimensions
        print(f"New dimensions: {resized_img.size}")

# Example usage
resize_image("../collections/2-proto_towers/media/tower12.png", "../collections/2-proto_towers/media/12.png", 768, 768)
