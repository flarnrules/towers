import cv2
import numpy as np
import os

INPUT_FOLDER = "/home/flarnrules/repos/towers/media/raw_formatted"
OUTPUT_FOLDER = "/home/flarnrules/repos/towers/media/dashboard_images"

def estimate_towers(thumbnail):
    gray = cv2.cvtColor(thumbnail, cv2.COLOR_BGR2GRAY)
    _, bin_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    tower_estimate = len(contours)
    return tower_estimate

def generate_dashboard(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    height, width, _ = image.shape
    
    # Thumbnail generation
    aspect_ratio = width / height
    if width > height:
        new_width = 128
        new_height = int(128 / aspect_ratio)
    else:
        new_height = 128
        new_width = int(128 * aspect_ratio)
    thumbnail = cv2.resize(image, (new_width, new_height))

    dashboard = np.ones((512, 512, 3), np.uint8) * 255
    start_y = (138 - new_height) // 2
    dashboard[start_y:start_y+new_height, 10:10+new_width] = thumbnail

    # RGB Graphs
    colors = ('b', 'g', 'r')
    for idx, col in enumerate(colors):
        hist = cv2.calcHist([image], [idx], None, [256], [0, 256])
        max_hist_value = int(hist.max())
        min_hist_value = int(hist.min())
        hist_height = 150
        for i in range(0, 256):
            value = hist_height * (hist[i] - min_hist_value) / (max_hist_value - min_hist_value)
            cv2.line(dashboard, (i + 362, 70 + idx * 50), (i + 362, 70 + idx * 50 - int(value[0])), tuple((255 if color != idx else 0) for color in range(3)), 1)

    # Extract and display sorted unique colors
    unique_colors, counts = np.unique(image.reshape(-1, 3), axis=0, return_counts=True)
    color_count_pairs = sorted(zip(unique_colors, counts), key=lambda x: x[1], reverse=True)
    sorted_colors = [color for color, _ in color_count_pairs[:20]]
    for idx, color in enumerate(sorted_colors):
        dashboard[420:470, idx*25:idx*25+25] = color

    # Info
    file_name = os.path.basename(image_path)
    cv2.putText(dashboard, file_name, (10, 490), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(dashboard, f"Dimensions: {width}x{height}", (10, 505), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(dashboard, f"Unique Colors: {len(unique_colors)}", (10, 520), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    tower_estimate = estimate_towers(thumbnail)
    cv2.putText(dashboard, f"Estimated Towers: {tower_estimate}", (10, 535), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    
    return dashboard

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for file_name in os.listdir(INPUT_FOLDER):
        print(f"Generating dashboard for: {file_name}")
        
        input_image_path = os.path.join(INPUT_FOLDER, file_name)
        output_image_path = os.path.join(OUTPUT_FOLDER, file_name)

        dashboard = generate_dashboard(input_image_path)
        cv2.imwrite(output_image_path, dashboard)

    print("Dashboard images generated successfully!")

if __name__ == "__main__":
    main()
