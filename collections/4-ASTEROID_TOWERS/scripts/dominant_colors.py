import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings("ignore")  # Suppress all warnings

def find_closest_emoji(color):
    emojis = {
        (255, 0, 0): '🟥',      # Red
        (0, 128, 0): '🟩',      # Green
        (0, 0, 255): '🟦',      # Blue
        (255, 255, 0): '🟨',    # Yellow
        (255, 165, 0): '🟧',    # Orange
        (128, 0, 128): '🟪',    # Purple
        (0, 0, 0): '⬛',        # Black
        (255, 255, 255): '⬜',  # White
        (165, 42, 42): '🟫',    # Brown
    }
    # Sort emojis by closest match
    closest_emoji = min(emojis.items(), key=lambda item: np.sqrt(sum((s - q) ** 2 for s, q in zip(item[0], color))))
    return closest_emoji[1]

def get_dominant_colors(image_path, num_clusters=5):
    try:
        img = Image.open(image_path).convert('RGB')
        data = np.array(img)
        data = data.reshape(-1, 3)

        kmeans = KMeans(n_clusters=num_clusters, n_init=10)
        kmeans.fit(data)
        unique_labels, counts = np.unique(kmeans.labels_, return_counts=True)
        dominant_colors = kmeans.cluster_centers_[unique_labels]

        sorted_colors = [x for _, x in sorted(zip(counts, dominant_colors), reverse=True, key=lambda x: x[0])]
        top_colors = [tuple(int(y) for y in x) for x in sorted_colors[:3]]
        return top_colors
    except FileNotFoundError:
        return None

def process_folder(folder_path):
    output = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            dominant_colors = get_dominant_colors(image_path)
            if dominant_colors:
                emojis = ''.join([find_closest_emoji(color) for color in dominant_colors])
                output.append(f"{filename} {emojis}")
            else:
                output.append(f"{filename} Error processing image")
    return output

# Usage
folder_path = input("Enter the path to your folder containing images: ")
results = process_folder(folder_path)
for result in results:
    print(result)
