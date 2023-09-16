import cv2
import os

def remove_numbers(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Invert the image and apply binary threshold
    _, bin_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Find contours in the image
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour to find potential number boxes
    for contour in contours:
        # Get the area of the contour
        area = cv2.contourArea(contour)

        # Get bounding rectangle around the contour
        rect = cv2.boundingRect(contour)
        aspect_ratio = float(rect[2]) / rect[3]
        
        # Check contour size and aspect ratio to identify number boxes
        if 50 < area < 3000 and 0.5 < aspect_ratio < 1.5:
            x, y, w, h = rect
            # Increase the size of the box slightly to ensure complete removal
            cv2.rectangle(image, (x-5, y-5), (x+w+5, y+h+5), (255, 255, 255), -1) # Fill the box with white

    # Save the modified image
    cv2.imwrite(output_path, image)

def main():
    input_folder = "../media/raw_formatted"
    output_folder = "../media/no_numbers"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input_folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            print(f"Removing numbers from: {filename}")
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            remove_numbers(input_image_path, output_image_path)

    print("Numbers removed successfully!")

if __name__ == "__main__":
    main()
