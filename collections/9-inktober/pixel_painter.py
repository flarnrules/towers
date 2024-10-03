import tkinter as tk
from tkinter import colorchooser, simpledialog
from PIL import Image, ImageDraw
from datetime import datetime
import json
import os
from helpers.file_helpers import get_file_names, save_json_metadata, calculate_iteration


# Function to load the prompt for the current day from the simplified 2024.json file
def load_prompt_for_day(day):
    with open('prompts/2024.json', 'r') as f:
        prompts_data = json.load(f)
        prompts = prompts_data["prompts"]
        if str(day) in prompts:
            return prompts[str(day)]  # Day 1 is at index 1
    return None

class PixelArtApp:
    def __init__(self, root, grid_size):
        self.root = root
        self.grid_size = grid_size
        self.pixel_size = 768 // grid_size
        self.current_color = "#000000"  # Default color is black

        # Set up the canvas for drawing
        self.canvas = tk.Canvas(root, width=768, height=768)
        self.canvas.pack()

        # Bind mouse click and drag events for painting
        self.canvas.bind("<Button-1>", self.paint_pixel)  # Click to paint
        self.canvas.bind("<B1-Motion>", self.paint_pixel)  # Drag to paint

        # Buttons for selecting color and saving the image
        self.color_button = tk.Button(root, text="Select Color", command=self.select_color)
        self.color_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        # Create an empty white image for saving the pixel art
        self.image = Image.new("RGB", (768, 768), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.draw_grid()

    def draw_grid(self):
        """Draw the grid on the canvas."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = i * self.pixel_size
                y1 = j * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def paint_pixel(self, event):
        """Paint a pixel on the canvas and in the image."""
        x, y = event.x, event.y
        i, j = x // self.pixel_size, y // self.pixel_size
        x1 = i * self.pixel_size
        y1 = j * self.pixel_size
        x2 = x1 + self.pixel_size
        y2 = y1 + self.pixel_size

        # Paint on the canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.current_color, outline="gray")
        # Paint on the image
        self.draw.rectangle([x1, y1, x2, y2], fill=self.current_color)

    def select_color(self):
        """Select a new color using a color chooser."""
        color = colorchooser.askcolor()[1]  # Returns a tuple (RGB, HEX)
        if color:
            self.current_color = color

    def save_image(self):
        """Save the image and corresponding JSON metadata."""
        # Set folder paths
        image_folder = "nfts/images"
        metadata_folder = "nfts/metadata"

        # Get next available file names for both the PNG and JSON files
        image_file, json_file = get_file_names(image_folder, metadata_folder)

        # Save the image
        self.image.save(image_file)
        print(f"Image saved as {image_file}")

        # Get the current day for Inktober
        day = datetime.now().day

        # Load the prompt for the current day from the JSON file
        prompt_value = load_prompt_for_day(day)
        if prompt_value is None:
            print(f"No prompt found for day {day}, metadata not saved.")
            return

        # Prompt the user for the artist's name
        artist = simpledialog.askstring("Input", "Enter artist's name:")
        if not artist:
            print("No artist name entered, metadata not saved.")
            return
        
        iteration = calculate_iteration(metadata_folder, prompt_value, artist) # iteration based on the same prompt and artist
        pixels = self.grid_size * self.grid_size  # Total number of pixels
        dimensions = f"{self.grid_size}x{self.grid_size}"  # Dimensions of the image
        prompt_name = f"{prompt_value}"

        # Pass the artist to save_json_metadata
        save_json_metadata(json_file, prompt_name, pixels, dimensions, artist, iteration)
        print(f"Metadata saved as {json_file}")

def main():
    grid_size = simpledialog.askinteger("Input", "Enter grid size (max 512):", minvalue=1, maxvalue=512)
    if grid_size is None:
        print("No grid size selected, exiting.")
        return

    root = tk.Tk()
    root.title("Pixel Painter")
    app = PixelArtApp(root, grid_size)
    root.mainloop()

if __name__ == "__main__":
    main()