import os
import numpy as np
from PIL import Image
import warnings

# v 0.01

warnings.filterwarnings("ignore")  # Suppress all warnings

def get_color_name(color):
    color_names = {
        (255, 0, 0): "Red",
        (0, 128, 0): "Green",
        (0, 0, 255): "Blue",
        (255, 255, 0): "Yellow",
        (255, 165, 0): "Orange",
        (128, 0, 128): "Purple",
        (0, 0, 0): "Black",
        (255, 255, 255): "White",
        (128, 0, 0): "Maroon",
        (128, 128, 128): "Gray",
        (192, 192, 192): "Silver",
        (128, 128, 0): "Olive",
        (0, 128, 128): "Teal",
        (0, 0, 128): "Navy",
        (0, 255, 255): "Aqua",
        (255, 0, 255): "Fuchsia"
    }
    closest_name = min(color_names.items(), key=lambda item: np.sqrt(sum((s - q) ** 2 for s, q in zip(item[0], color))))
    return closest_name[1]

def get_most_prominent_color(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
        data = np.array(img)
        colors, counts = np.unique(data.reshape(-1, data.shape[2]), axis=0, return_counts=True)
        most_frequent_color = tuple(colors[np.argmax(counts)])
        return most_frequent_color
    except FileNotFoundError:
        return None

def process_folder(folder_path):
    output = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            most_prominent_color = get_most_prominent_color(image_path)
            if most_prominent_color:
                color_name = get_color_name(most_prominent_color)
                output.append(f"{filename}: {color_name}")
            else:
                output.append(f"{filename}: Error processing image")
    return output

# Usage
folder_path = input("Enter the path to your folder containing images: ")
results = process_folder(folder_path)
for result in results:
    print(result)
