import random as rndm

class Plants:
    def __init__(self, canvas, rows, cols, cell_size, circle_radius=15):
        self.initial_offset = 30
        center_x = self.initial_offset + cell_size // 2
        center_y = self.initial_offset + cell_size // 2
        self.plants_type = ["R", "G", "B", "Skip", "Skip", "Skip"]

        # Populate the grid with canvases and draw circles on them
        for i in range(rows):
            for j in range(cols):
                canvas.grid(row=i, column=j)
                
                # Draw a circle in the canvas
                self.draw_circle(canvas, center_x, center_y, circle_radius)

                # Calculate the next center of the circle
                center_y += cell_size
            
            center_x += cell_size
            center_y = self.initial_offset + cell_size // 2

    def draw_circle(self, canvas, x, y, r):
        """Draw a circle with given radius and center coordinates."""
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill="white")
        plant_to_be_placed = rndm.choice(self.plants_type)
        if plant_to_be_placed != "Skip":
            txt_color = None
            if plant_to_be_placed == "R":
                txt_color = "red"
            elif plant_to_be_placed == "G":
                txt_color = "green"
            elif plant_to_be_placed == "B":
                txt_color = "blue"
            canvas.create_text(x, y, text=plant_to_be_placed, fill=txt_color, font=("Arial", 15))

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")
