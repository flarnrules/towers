import cv2

def draw_square(image_path, output_path, size):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Calculate center of the image
    center_y, center_x = height // 2, width // 2

    # Calculate top-left and bottom-right coordinates for the square
    top_left = (center_x - size // 2, center_y - size // 2)
    bottom_right = (center_x + size // 2, center_y + size // 2)

    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)  # Drawing a red square

    cv2.imwrite(output_path, image)

def main():
    image_path = input("Enter the path of your image: ")
    size = int(input("Enter the size of the square: "))
    output_path = "output_with_square.png"
    
    draw_square(image_path, output_path, size)
    print(f"Square drawn on image and saved as {output_path}")

if __name__ == "__main__":
    main()
