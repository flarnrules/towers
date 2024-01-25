import cv2
import numpy as np

def create_floor_collision_js(image_path, js_output_path, tile_size=2):
    # Load the image in color mode
    image = cv2.imread(image_path)

    # Initialize the floor collision array
    floor_collisions = []

    # Process the image in tiles of size 2x2 pixels
    for row in range(0, image.shape[0], tile_size):
        for col in range(0, image.shape[1], tile_size):
            # Extract the tile
            tile = image[row:row + tile_size, col:col + tile_size]

            # Calculate the percentage of blue pixels in the tile
            blue_pixels = np.sum(np.all(tile == [255, 0, 0], axis=-1))
            total_pixels = tile_size * tile_size
            blue_percentage = blue_pixels / total_pixels

            # Determine if the tile is predominantly blue
            floor_collisions.append(1 if blue_percentage > 0.5 else 0)

    # Convert the floor collisions to a JS array
    js_array = f"const floorCollisions = {floor_collisions};"

    # Write the JS array to file
    with open(js_output_path, 'w') as js_file:
        js_file.write(js_array)

    print(f"Floor collision JS file has been created at {js_output_path}")

# Usage
image_path = 'media/platformer/img/collisions.png'  # Replace with your image path
js_output_path = 'media/platformer/js/data/collisions.js'  # Replace with the desired output JS file path
create_floor_collision_js(image_path, js_output_path)
