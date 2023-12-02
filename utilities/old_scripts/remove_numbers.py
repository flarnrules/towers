import cv2
import os

def remove_numbers(input_image_path, output_image_path):
    image = cv2.imread(input_image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding to get binary image
    _, bin_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and fill in small ones
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # These area values can be adjusted based on the size of the numbers in your images.
        if 50 < area < 3000: 
            rect = cv2.boundingRect(contour)
            aspect_ratio = float(rect[2]) / rect[3]
            
            # Check if the contour is more rectangular (indicative of a number box)
            if 0.2 < aspect_ratio < 2:
                cv2.drawContours(image, [contour], -1, (255, 255, 255), -1)

    cv2.imwrite(output_image_path, image)

def main():
    input_folder = "../media/raw_formatted"
    output_folder = "../media/number_removed"
    
    # Ensure output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            print(f"Processing: {filename}")
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            
            remove_numbers(input_image_path, output_image_path)
    
    print("Number removal completed!")

if __name__ == "__main__":
    main()
