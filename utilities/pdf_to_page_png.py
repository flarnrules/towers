from PIL import Image
from pdf2image import convert_from_path
import os

def pdf_to_png(input_path, output_folder, start_page_num):
    # Ensure the output directory exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF to list of images
    pages = convert_from_path(input_path, dpi=300)  # Adjust dpi as needed

    output_paths = []
    for index, page in enumerate(pages, start=start_page_num):
        output_path = os.path.join(output_folder, f"{index}.png")
        page.save(output_path, "PNG")
        output_paths.append(output_path)

    return output_paths

def process_image(image_path, crop_box):
    with Image.open(image_path) as img:
        # Rotate the image by 180 degrees to correct the orientation
        img = img.rotate(180)

        # Crop the image using the provided crop_box
        img = img.crop(crop_box)

        # Save the processed image
        img.save(image_path)

def main():
    input_folder = "../media/raw"
    output_folder = "../media/raw_formatted"
    index = 1
    global_page_num = 1

    # Define the cropping box (left, upper, right, lower)
    # Adjust these values based on your notebook's dimensions after scanning
    crop_box = (75, 275, 2575, 3520)

    while True:
        input_pdf_path = os.path.join(input_folder, f"SCN_{index:04}.pdf")

        # If the file doesn't exist, we assume the end of the sequence
        if not os.path.exists(input_pdf_path):
            break

        print(f"Converting {input_pdf_path} to PNG...")
        converted_images = pdf_to_png(input_pdf_path, output_folder, global_page_num)
        global_page_num += len(converted_images)

        for image_path in converted_images:
            print(f"Processing image: {image_path}")
            process_image(image_path, crop_box)

        index += 1

    print("All images processed successfully!")

if __name__ == "__main__":
    main()
