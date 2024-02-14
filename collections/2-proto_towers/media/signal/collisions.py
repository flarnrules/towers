from PIL import Image
import json

def is_tile_of_color(image, x, y, tile_size, color):
    """Check if the tile at (x, y) is of a specific color."""
    for i in range(tile_size):
        for j in range(tile_size):
            if image.getpixel((x + i, y + j)) != color:
                return False
    return True

def generate_collision_map(image_path, json_path, tile_size=6):
    # Load the image and convert to RGB mode
    image = Image.open(image_path).convert('RGB')

    walkable = []
    trigger = []

    blue = (0, 0, 255)  # Walkable areas
    red = (255, 0, 0)   # Trigger spot

    width, height = image.size
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            # Use the top-left pixel of each tile for color comparison
            if is_tile_of_color(image, x, y, tile_size, blue):
                walkable.append([x // tile_size, y // tile_size])
            elif is_tile_of_color(image, x, y, tile_size, red):
                trigger.append([x // tile_size, y // tile_size])

    # Assuming a single trigger point for simplicity
    trigger_point = trigger[0] if trigger else None

    collision_map = {
        'walkable': walkable,
        'trigger': trigger_point
    }

    with open(json_path, 'w') as file:
        json.dump(collision_map, file, indent=4)

    print(f"Collision map generated with {len(walkable)} walkable points and trigger point at {trigger_point}")


# Paths to your image and output JSON file
image_path = '341/outside_collision_map.png' # Update with the path to your image
json_path = '341/outside_collision_map.json' # Update with your desired output path

generate_collision_map(image_path, json_path)
