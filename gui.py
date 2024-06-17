import tkinter as tk
import random
import car
import grid
import plants

class BuildMainGui():
    def __init__(self, root, rows=6, cols=6, cell_size=100, car_size=10, num_cars=3):
        self.rows = rows
        self.cols = cols
        self.car_size = car_size
        self.root = root
        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()

        # Create grid gui.
        self.grid_object = grid.Grid(self.canvas, rows, cols, cell_size)
        
        # Create car gui.
        self.car_object = car.Car(root, self.canvas, rows, cols, cell_size, car_size)

        # Create plants gui.
        self.plants_object = plants.Plants(self.canvas, rows, cols, cell_size)
        self.move_cars_automatically()        


    def move_cars_automatically(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for i, pos in enumerate(self.car_object.car_positions):
            direction = random.choice(directions)
            new_position = [pos[0] + direction[0], pos[1] + direction[1]]

            # Ensure the new position is within bounds
            if 0 <= new_position[0] < self.rows and 0 <= new_position[1] < self.cols:
                self.car_object.car_positions[i] = new_position

            x, y = self.car_object.get_car_coordinates(self.car_object.car_positions[i])
            self.canvas.coords(self.car_object.cars[i], 
                x - self.car_size, y - self.car_size,
                x + self.car_size, y + self.car_size
            )

        self.root.after(500, self.move_cars_automatically)  # Repeat every 500ms


# Create the main application window
root = tk.Tk()
root.title("Eyantra Robotic Competition - Feeder Weeder")

# Initialize the CarGridApp
app = BuildMainGui(root)

# Start the main event loop
root.mainloop()
