import cv2
import os

def preprocess_image(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    # Morphological closing operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    return closed

def remove_numbers_and_corners(input_path, output_path):
    # Read the image
    image = cv2.imread(input_path)
    preprocessed = preprocess_image(image)

    # Find contours on the preprocessed image
    contours, _ = cv2.findContours(preprocessed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Compute the bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # Condition to check if it's likely a number
        if 100 < w * h < 50000:
            cv2.drawContours(image, [contour], -1, (255, 255, 255), -1)

        # Condition to check if it's likely a corner
        if 5 < w * h < 100:
            cv2.drawContours(image, [contour], -1, (255, 255, 255), -1)

    # Save the processed image
    cv2.imwrite(output_path, image)

def main():
    input_folder = "../media/raw_formatted"
    output_folder = "../media/no_numbers"

    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            print(f"Removing numbers and corners from: {filename}")
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            remove_numbers_and_corners(input_image_path, output_image_path)

if __name__ == "__main__":
    main()
