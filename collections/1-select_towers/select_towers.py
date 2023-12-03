#from ren_gen_met.py import create_metadata_and_images
import os
import re
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class TowerTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tower Image Processor")
        self.geometry("1000x645")  # Set window size

        self.container = tk.Frame(self)  # New containing frame
        self.container.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.container, width=800, height=600)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.thumbnail_frame = tk.Frame(self.container)
        self.thumbnail_frame.grid(row=0, column=1, sticky="ns")

        self.button_frame = tk.Frame(self.container)  # Changed parent to self.container
        self.button_frame.grid(row=1, columnspan=2, sticky="ew")  # Changed pack to grid

        self.save_button = tk.Button(self.button_frame, text="Save NFT images", command=self.save_NFT_images)
        self.save_button.grid(row=0, column=0, padx=5, pady=5)  # changed pack to grid
        
        self.next_button = tk.Button(self.button_frame, text="Load Next Image", command=self.load_next_image_wrapper)
        self.next_button.grid(row=0, column=1, padx=5, pady=5)  # changed pack to grid

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.menu.add_command(label="Open", command=self.open_file_dialog)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.selection_rectangle = None
        self.start_x = None
        self.start_y = None
        
        # List to hold references to PhotoImage objects
        self.tk_images = []
        self.current_row = 0
        self.current_column = 0
        self.max_columns = 4
        
        # Adjust the column widths
        self.container.grid_columnconfigure(0, weight=1)  # Allocate more space to column 0 (main canvas)
        self.container.grid_columnconfigure(1, weight=0)  # Allocate less space to column 1 (thumbnail_frame)

        self.rectangles = []
        self.image_sections = []
        self.rectangles_coords = []

        self.current_image_number = None

    def open_image(self, image_path):
        self.original_image = Image.open(image_path)
        
        image_number_match = re.search(r'(\d+)\.png$', os.path.basename(image_path))
        if image_number_match:
            self.current_image_number = int(image_number_match.group(1))
        
        # Calculate the new width to maintain the aspect ratio
        new_height = self.canvas.winfo_height()
        aspect_ratio = self.original_image.width / self.original_image.height
        new_width = int(new_height * aspect_ratio)
        
        # Resize the image
        display_image = self.original_image.resize((new_width, new_height), Image.LANCZOS)
        
        self.tk_image = ImageTk.PhotoImage(display_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
    
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="../../media/preprocessed")
        if file_path:
            self.open_image(file_path)
    

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if not self.selection_rectangle:
            self.selection_rectangle = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="cyan")

    def on_mouse_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)

        self.canvas.coords(self.selection_rectangle, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x = self.canvas.canvasx(event.x)
        end_y = self.canvas.canvasy(event.y)
        
        # Create a new rectangle on the canvas
        rect_id = self.canvas.create_rectangle(
            self.start_x, self.start_y, end_x, end_y, outline="blue"
        )
        self.rectangles.append(rect_id)  # Store the rectangle ID to keep track of it
        
        # Adjust coordinates according to the scaling factor
        scaling_factor = self.get_scaling_factor()
        coords = (int(self.start_x / scaling_factor), int(self.start_y / scaling_factor),
              int(end_x / scaling_factor), int(end_y / scaling_factor))
        self.rectangles_coords.append(coords)  # Save the coordinates
        
        # Extract the image section
        image_section = self.original_image.crop(coords)
        
        # Create a thumbnail
        thumbnail_size = (100, 100)  # Adjust size as needed
        image_section.thumbnail(thumbnail_size, Image.LANCZOS)
        self.image_sections.append(image_section)
        
        # Display the thumbnail
        tk_thumbnail = ImageTk.PhotoImage(image_section)
        self.tk_images.append(tk_thumbnail)  # Keep reference to prevent garbage collection
        thumbnail_label = tk.Label(self.thumbnail_frame, image=tk_thumbnail)
        thumbnail_label.grid(row=self.current_row, column=self.current_column, padx=5, pady=5)  # Reverted back to original column logic

        # Update row and column for next thumbnail
        self.current_column += 1
        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1

    
    def get_scaling_factor(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        scaling_factor = min(canvas_width / self.original_image.width, canvas_height / self.original_image.height)
        return scaling_factor
    
    def save_NFT_images(self):
        tower_images_dir = "originals"
        os.makedirs(tower_images_dir, exist_ok=True)  # Create directory if it doesn't exist
        
        for i, (coords, image_section) in enumerate(zip(self.rectangles_coords, self.image_sections)):
            # Formulate the file name according to the specified convention
            file_name = f"{self.current_image_number}_{i + 1}.png"
            file_path = os.path.join(tower_images_dir, file_name)
            
            # Extract the corresponding region from the original image
            original_region = self.original_image.crop(coords)
            original_region.save(file_path)
    
    
    def load_next_image_wrapper(self):
        if self.current_image_number is not None:
            self.current_image_number += 1  # Increment to the next image number
            next_image_path = f"../../media/preprocessed/{self.current_image_number}.png"
            self.load_next_image(next_image_path)
        else:
            print("No current image number available.")
    
    
    def load_next_image(self, image_path):
        self.selection_rectangle = None  # Reset the selection rectangle
        
        self.original_image = Image.open(image_path)
        
        # Reset the canvas and other related variables if necessary
        self.canvas.delete("all")
        self.tk_images.clear()
        self.image_sections.clear()
        self.rectangles_coords.clear()  # Assuming you have this list to hold rectangle coordinates
        self.current_row = 0
        self.current_column = 0
        
        # Rebind the event handlers in case they were lost
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        # Get the dimensions of the canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Calculate the scaling factor
        scaling_factor = min(canvas_width / self.original_image.width, canvas_height / self.original_image.height)
        
        # Create a temporary resized image for display
        display_image = self.original_image.resize((int(self.original_image.width * scaling_factor), int(self.original_image.height * scaling_factor)), Image.LANCZOS)
        
        self.tk_image = ImageTk.PhotoImage(display_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)



if __name__ == "__main__":
    app = TowerTool()
    app.mainloop()


## Calls the script that creates or populaes the images
## folder and properly names the images according to requirements
## also creates an empty list for each properly named .json file
source_directory = "originals"
images_directory = "images"
metadata_directory = "metadata"
#create_metadata_and_images(source_directory, images_directory, metadata_directory)
