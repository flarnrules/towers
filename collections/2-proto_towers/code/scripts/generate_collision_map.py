import json
import cv2
import numpy as np

def create_collision_map(image_path, output_path):
    # Load the image in color mode
    image = cv2.imread(image_path)

    # Define the color range for blue paths
    lower_blue = np.array([255, 0, 0])
    upper_blue = np.array([255, 0, 0])

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

def create_sequenced_collision_map(collision_map):
    sequence_number = 1
    sequenced_map = []
    for row in collision_map:
        sequenced_row = []
        for cell in row:
            if cell:  # Walkable
                sequenced_row.append(sequence_number)
                sequence_number += 1
            else:
                sequenced_row.append(0)  # Not walkable
        sequenced_map.append(sequenced_row)
    return sequenced_map

# Usage
image_path = 'media/wip/305/305.png'  # Replace with your image path
output_path = 'media/wip/305/305_map.png'  # Replace with the desired output image path
collision_map = create_collision_map(image_path, output_path)

# Convert the collision map to a sequenced collision map
sequenced_collision_map = create_sequenced_collision_map(collision_map)

# Convert the sequenced collision map to JSON
formatted_json_lines = ["[" + ", ".join(map(str, row)) + "]" for row in sequenced_collision_map]
formatted_json = "[\n" + ",\n".join(formatted_json_lines) + "\n]"

# Write to file
json_output_path = 'media/wip/305/305.json'  # Set the path for the JSON file
with open(json_output_path, 'w') as json_file:
    json_file.write(formatted_json)

print(f"Sequenced collision map JSON file has been created at {json_output_path}")
