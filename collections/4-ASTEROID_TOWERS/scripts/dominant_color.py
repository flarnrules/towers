from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_dominant_color(image_path, num_clusters=3):
    # Load the image and convert to sRGB
    img = Image.open(image_path).convert('RGB')
    img = img.resize((50, 50))  # Resize to reduce computation

    # Convert image data to a 2D numpy array.
    data = np.array(img)
    data = data.reshape(-1, 3)

    # Cluster colors using K-means
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(data)
    dominant_color = kmeans.cluster_centers_[np.argmax(np.bincount(kmeans.labels_))]

    # Normalize and convert to integer
    dominant_color = tuple(int(x) for x in dominant_color)
    return dominant_color

def find_closest_emoji(dominant_color):
    # Define emoji colors and corresponding emojis
    emojis = {
        (255, 0, 0): '🟥',  # Red
        (0, 128, 0): '🟩',  # Green
        (0, 0, 255): '🟦',  # Blue
        (255, 255, 0): '🟨',  # Yellow
        (255, 165, 0): '🟧',  # Orange
        (128, 0, 128): '🟪',  # Purple
        (0, 0, 0): '⬛',  # Black
        (255, 255, 255): '⬜',  # White
    }

    # Find the closest emoji
    closest_emoji = min(emojis.keys(), key=lambda color: sum((s - q) ** 2 for s, q in zip(color, dominant_color)))
    return emojis[closest_emoji]

# Usage
image_path = '../inscriptions/files/ASTEROID_TOWER_7.png'  # Update this with your image path
dominant_color = get_dominant_color(image_path)
emoji = find_closest_emoji(dominant_color)
print(f"Dominant Color: {dominant_color}, Closest Emoji: {emoji}")
