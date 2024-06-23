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
        self.canvas = tk.Canvas(root, width=50+cols * cell_size, height=50+rows * cell_size, bg="white")
        self.canvas.pack()
        self.system_state = "GET_INFO"
        self.total_cars = 3
        self.cars_objects_list = []
        self.car_colors = ["red", "green", "blue"]

        # Create grid gui.
        self.grid_object = grid.Grid(self.canvas, rows, cols, cell_size)
        
        # Create car gui. 
        initial_pos = [[0, 1], [cols-3, rows], [cols, 1]]
        for i in range(0, self.total_cars):
            instance = car.Car(root, 
                               self.canvas, 
                               rows, cols, cell_size, car_size, 
                               initial_pos[i][0], initial_pos[i][1], 
                               self.car_colors[i])            
            self.cars_objects_list.append(instance)

        # Create plants gui.
        self.plants_object = plants.Plants(self.canvas, rows, cols, cell_size)


    def move_cars_automatically(self):
        # Calculte where to move the car next
        for current_car in self.cars_objects_list:
            current_car.next_move()

        # Move the car on the canvas the gui
        for current_car in self.cars_objects_list:
            new_position = [current_car.x_pos, current_car.y_pos]

            # Ensure the new position is within bounds
            if (0 <= new_position[0] < self.rows) and (0 <= new_position[1] < self.cols):
                x, y = current_car.get_car_coordinates(new_position)
                self.canvas.coords(current_car.the_car, 
                    x - current_car.corner_vector[0], y - current_car.corner_vector[1],
                    x + current_car.corner_vector[0], y + current_car.corner_vector[1]
                )
            else:
                print("Invalid Car Position", new_position[0], new_position[1])

        self.root.after(10, self.move_cars_automatically)  # Scedule move_cars_automatically every 10ms

# Create the main application window
root = tk.Tk()
root.title("Eyantra Robotic Competition - Feeder Weeder")

# Initialize the CarGridApp
app = BuildMainGui(root)

# Calculate car will move in the next time scale.
# app.move_cars_automatically()

# Start the main event loop
root.mainloop()
