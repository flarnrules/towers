import json
import cv2
import numpy as np

def create_collision_map(image_path, output_path):
    # Load the image in color mode
    image = cv2.imread(image_path)

    # Define the color range for blue paths
    lower_blue = np.array([100, 0, 0])
    upper_blue = np.array([255, 100, 100])

    # Create a mask that captures areas of the image that are blue
    mask = cv2.inRange(image, lower_blue, upper_blue)

    # Initialize the collision map as a 2D array of False values
    collision_map = np.full((image.shape[0], image.shape[1]), False)

    # Update the collision map to True where the mask is white (blue areas)
    collision_map[mask > 0] = True

    # Visual confirmation: Create an image where walkable areas are white and non-walkable areas are black
    visual_map = np.zeros_like(image)
    visual_map[collision_map] = [255, 255, 255]
    cv2.imwrite(output_path, visual_map)

    return collision_map

# Usage
image_path = 'media/wip/276/276.png'  # Replace with your image path
output_path = 'media/wip/276/276_map.png'  # Replace with the desired output image path
collision_map = create_collision_map(image_path, output_path)

# Now, collision_map is a 2D boolean array where True represents walkable areas
# And a visual map has been saved to output_path
# Convert the collision map to a 2D array of 0s and 1s
collision_map_numeric = [[1 if cell else 0 for cell in row] for row in collision_map]

# Manually format the JSON string
formatted_json_lines = ["[" + ", ".join(map(str, row)) + "]" for row in collision_map_numeric]
formatted_json = "[\n" + ",\n".join(formatted_json_lines) + "\n]"

# Write to file
json_output_path = 'media/wip/276/collisionMap.json'  # Set the path for the JSON file
with open(json_output_path, 'w') as json_file:
    json_file.write(formatted_json)

print(f"Collision map JSON file has been created at {json_output_path}")