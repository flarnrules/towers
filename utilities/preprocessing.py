import cv2
import os
import numpy as np

def is_grayscale(img):
    """Check if an image is grayscale or colored."""
    # If all three color channels are identical, then the image is grayscale
    return cv2.countNonZero(cv2.subtract(img[:,:,0], img[:,:,1])) == 0 and cv2.countNonZero(cv2.subtract(img[:,:,0], img[:,:,2])) == 0

def darken_grays(image):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Increase the intensity of the V channel to darken grays
    v_channel = hsv[:, :, 2]
    bool_mask = np.logical_and(v_channel > 50, v_channel < 200)  # targeting grayish values
    hsv[bool_mask, 2] = hsv[bool_mask, 2] * 0.75  # reduce the brightness of these pixels by 25%
    
    # Convert back to BGR color space
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def enhance_image(image):
    # Reduce noise using bilateral filter
    denoised = cv2.bilateralFilter(image, 5, 50, 50)
    
    # Darken grays
    darkened = darken_grays(denoised)

    # Slightly sharpen the image
    kernel = np.array([[0, -0.25, 0],
                       [-0.25, 2, -0.25],
                       [0, -0.25, 0]])
    sharpened = cv2.filter2D(darkened, -1, kernel)

    return sharpened




def main():
    input_folder = "../media/raw_formatted"
    output_folder = "../media/preprocessed"
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            print(f"Enhancing: {filename}")
            
            # Read the image
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            
            # Enhance the image
            enhanced_image = enhance_image(image)
            
            # Save the enhanced image
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, enhanced_image)

if __name__ == "__main__":
    main()
