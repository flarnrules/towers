import tkinter as tk
from tkinter import colorchooser, simpledialog
from PIL import Image, ImageDraw

class PixelArtApp:
    def __init__(self, root, grid_size):
        self.root = root
        self.grid_size = grid_size
        self.pixel_size = 512 // grid_size  # Ensure the canvas is always 512x512
        self.current_color = "#000000"  # Default color is black

        self.canvas = tk.Canvas(root, width=512, height=512)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.paint_pixel)

        self.color_button = tk.Button(root, text="Select Color", command=self.select_color)
        self.color_button.pack()

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image)
        self.save_button.pack()

        self.image = Image.new("RGB", (512, 512), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.draw_grid()

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x1 = i * self.pixel_size
                y1 = j * self.pixel_size
                x2 = x1 + self.pixel_size
                y2 = y1 + self.pixel_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

    def paint_pixel(self, event):
        x, y = event.x, event.y
        i, j = x // self.pixel_size, y // self.pixel_size
        x1 = i * self.pixel_size
        y1 = j * self.pixel_size
        x2 = x1 + self.pixel_size
        y2 = y1 + self.pixel_size

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.current_color, outline="gray")
        self.draw.rectangle([x1, y1, x2, y2], fill=self.current_color)

    def select_color(self):
        color = colorchooser.askcolor()[1]  # Returns a tuple (RGB, HEX)
        if color:
            self.current_color = color

    def save_image(self):
        self.image.save("proto_tower_x.png")
        print("Image saved as proto_tower_x.png")

def main():
    grid_size = simpledialog.askinteger("Input", "Enter grid size (max 512):", minvalue=1, maxvalue=512)
    if grid_size is None:
        print("No grid size selected, exiting.")
        return

    root = tk.Tk()
    root.title("Pixel Art Maker")
    app = PixelArtApp(root, grid_size)
    root.mainloop()

if __name__ == "__main__":
    main()