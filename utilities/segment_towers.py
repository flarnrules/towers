import cv2
import os

def extract_towers(input_image_path, output_folder):
    # Read the image using OpenCV
    image = cv2.imread(input_image_path)
    
    # Remove the handwritten number
    image = remove_number(image)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding the image to binarize
    _, thresh1 = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Detecting contours
    contours, _ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ensure the output directory exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    extracted_towers = []

    min_tower_area = 25000  # Adjust as needed

    for contour in contours:
        if cv2.contourArea(contour) < min_tower_area:
            continue
        
        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract tower image
        tower = image[y:y+h, x:x+w]
        
        extracted_towers.append(tower)

    return extracted_towers

def remove_number(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)
        aspect_ratio = float(w) / h

        # More specific criteria to identify the numbers
        if 2500 < area < 5000 and 0.7 < aspect_ratio < 1.3:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)

    return image


def main():
    input_folder = "../media/raw_formatted"
    output_folder = "../media/tower_images"
    
    overall_tower_count = 0
    
    # Process each PNG image in the input_folder
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.png'):
            print(f"Processing: {filename}")
            
            input_image_path = os.path.join(input_folder, filename)
            extracted_towers = extract_towers(input_image_path, output_folder)
            
            page_number = int(filename.split('.')[0])
            
            for tower in extracted_towers:
                overall_tower_count += 1
                output_path = os.path.join(output_folder, f"{page_number}_{overall_tower_count}.png")
                cv2.imwrite(output_path, tower)

    print("Towers extracted successfully!")

if __name__ == "__main__":
    main()
