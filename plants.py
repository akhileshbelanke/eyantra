import random as rndm

class Plants:
    def __init__(self, canvas, rows, cols, cell_size, circle_radius=15):
        self.initial_offset = 30
        center_x = self.initial_offset + cell_size // 2
        center_y = self.initial_offset + cell_size // 2
        self.plants_type = ["red", "green", "blue", "Skip"]
        self.plants_positions = []
        self.temp_plant_struct = {
            "COLOR": None,
            "VISITED": None,
        }
        # Populate the grid with canvases and draw circles on them
        for i in range(rows):
            for j in range(cols):
                canvas.grid(row=i, column=j)
                
                # Draw a circle in the canvas
                self.temp_plant_struct = {
                    "COLOR": self.draw_circle_place_plant(canvas, center_x, center_y, circle_radius),
                    "VISITED": None,
                }

                # Calculate the next center of the circle
                center_x += cell_size
                self.plants_positions.append(self.temp_plant_struct)

            center_x = self.initial_offset + cell_size // 2
            center_y += cell_size
    
    def feed_weed_the_plant(self, canvas, action, x, y, r, plant_color):
        if plant_color != "green":
            canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill=plant_color)
        else:
            canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill=plant_color)
        
    def draw_circle_place_plant(self, canvas, x, y, r):
        """Draw a circle with given radius and center coordinates."""
        canvas.create_oval(x - r, y - r, x + r, y + r, outline="black", fill="white")
        plant_to_be_placed = rndm.choice(self.plants_type)
        # plant_to_be_placed = "red"
        if plant_to_be_placed != "Skip":
            canvas.create_text(x, y, text=plant_to_be_placed, fill=plant_to_be_placed, font=("Arial", 15))
        
        return plant_to_be_placed

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")
