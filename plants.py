class Plants:
    def __init__(self, canvas, rows, cols, cell_size, circle_radius=15):
        center_x = cell_size // 2
        center_y = cell_size // 2
        # Populate the grid with canvases and draw circles on them
        for i in range(rows):
            for j in range(cols):
                canvas.grid(row=i, column=j)
                
                # Draw a circle in the canvas
                self.draw_circle(canvas, center_x, center_y, circle_radius)

                # Calculate the next center of the circle
                center_y += cell_size
            
            center_x += cell_size
            center_y = cell_size // 2

    def draw_circle(self, canvas, x, y, r):
        """Draw a circle with given radius and center coordinates."""
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill="white")


if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")
