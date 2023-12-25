from PIL import Image

def clean_and_center_image(image_path, output_path, threshold=240):
    # Load the image
    image = Image.open(image_path)

    # Convert image to grayscale for thresholding
    gray_image = image.convert('L')

    # Apply the threshold to normalize the white background
    white_normalized_image = gray_image.point(lambda x: 255 if x > threshold else x)

    # Convert back to RGB
    white_normalized_image = white_normalized_image.convert('RGB')

    # Get the current size of the image
    current_width, current_height = white_normalized_image.size

    # Determine the size of the new square canvas
    new_dimension = max(current_width, current_height)

    # Create a new white square image
    square_canvas = Image.new('RGB', (new_dimension, new_dimension), (255, 255, 255))

    # Calculate the position to paste the drawing on the square canvas
    left = (new_dimension - current_width) // 2
    top = (new_dimension - current_height) // 2

    # Paste the image onto the square canvas
    square_canvas.paste(white_normalized_image, (left, top))

    # Save the final cleaned and centered image
    square_canvas.save(output_path)

# Example usage:
image_path = '../collections/1-select_towers/images/1.png'  # Replace with your image path
output_path = '../collections/1-select_towers/cleaned_images/1.png'  # Replace with your desired output path
clean_and_center_image(image_path, output_path)