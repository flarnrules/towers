from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import os

def get_dominant_color(image_path, num_clusters=3):
    try:
        # Load the image and convert to sRGB
        img = Image.open(image_path).convert('RGB')
        img = img.resize((50, 50))  # Resize to reduce computation
        data = np.array(img)
        data = data.reshape(-1, 3)

        # Cluster colors using K-means
        kmeans = KMeans(n_clusters=num_clusters)
        kmeans.fit(data)
        dominant_color = kmeans.cluster_centers_[np.argmax(np.bincount(kmeans.labels_))]

        # Normalize and convert to integer
        dominant_color = tuple(int(x) for x in dominant_color)
        return dominant_color
    except FileNotFoundError:
        print(f"No file found at {image_path}. Please check the path and try again.")
        return None

def find_closest_emoji(dominant_color):
    # Define emoji colors and corresponding emojis
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
        (128, 128, 128): '⬜',  # Grey
        (255, 192, 203): '🟥',  # Pink
        (0, 255, 255): '🟦',    # Cyan
        (255, 105, 180): '🟥',  # Hot Pink
        (75, 0, 130): '🟪'      # Indigo
    }

    # Find the closest emoji
    closest_emoji = min(emojis.keys(), key=lambda color: sum((s - q) ** 2 for s, q in zip(color, dominant_color)))
    return emojis[closest_emoji]

# Get user input for image path
image_path = input("Enter the path to your image: ")

# Validate file existence before proceeding
if os.path.exists(image_path):
    dominant_color = get_dominant_color(image_path)
    if dominant_color:
        emoji = find_closest_emoji(dominant_color)
        print(f"Dominant Color: {dominant_color}, Closest Emoji: {emoji}")
else:
    print("File does not exist. Please check the path and try again.")
