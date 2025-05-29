import tkinter as tk

class EraseCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Erase Canvas")

        # Create the canvas
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg="black")
        self.canvas.pack()

        # Create reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_canvas)
        self.reset_button.pack()

        # Draw grid pattern of blue squares
        self.grid_size = 30  # Size of each grid cell
        self.squares = {}  # Store references to each square for erasing

        self.draw_boxes()  # Call function to initially draw boxes

        # Bind left mouse button for erasing
        self.canvas.bind("<B1-Motion>", self.erase)

    def draw_boxes(self):
        """Draw grid pattern of blue squares."""
        for x in range(0, 500, self.grid_size):
            for y in range(0, 500, self.grid_size):
                square = self.canvas.create_rectangle(x, y, x+self.grid_size, y+self.grid_size, fill="blue", outline="black")
                self.squares[(x, y)] = square  # Store square reference

    def erase(self, event):
        """Erase grid squares where the mouse moves."""
        x = (event.x // self.grid_size) * self.grid_size
        y = (event.y // self.grid_size) * self.grid_size

        if (x, y) in self.squares:
            self.canvas.itemconfig(self.squares[(x, y)], fill="black")  # Change square color to match background

    def reset_canvas(self):
        """Reset canvas by redrawing the blue grid boxes."""
        self.squares.clear()  # Remove previous squares
        self.canvas.delete("all")  # Clear canvas
        self.draw_boxes()  # Redraw all squares

# Initialize Tkinter window
root = tk.Tk()

# Create an instance of EraseCanvas class
erase_canvas_app = EraseCanvas(root)

# Run the application
root.mainloop()