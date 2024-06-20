import tkinter as tk
import random
import car
import grid
import plants

class BuildMainGui():
    def __init__(self, root, rows=6, cols=6, cell_size=110, car_size=10, num_cars=3):
        self.rows = rows
        self.cols = cols
        self.car_size = car_size
        self.root = root
        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size, bg="white")
        self.canvas.pack()
        self.system_state = "GET_INFO"

        # Create grid gui.
        self.grid_object = grid.Grid(self.canvas, rows, cols, cell_size)
        
        # Create car gui. 
        initial_pos = [[1, 0], [1, cols], [rows, cols-3]]
        self.car1 = car.Car(root, self.canvas, rows, cols, cell_size, car_size, initial_pos[0][0], initial_pos[0][1], "red")
        self.car2 = car.Car(root, self.canvas, rows, cols, cell_size, car_size, initial_pos[1][0], initial_pos[1][1], "blue")
        self.car3 = car.Car(root, self.canvas, rows, cols, cell_size, car_size, initial_pos[2][0], initial_pos[2][1], "green")

        # Create plants gui.
        self.plants_object = plants.Plants(self.canvas, rows, cols, cell_size)


    def move_cars_automatically(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # Calculte where to move the car next
        for current_car in [self.car1, self.car2, self.car3]:
            current_car.next_move()

        # Move the car on the canvas the gui
        for current_car in [self.car1, self.car2, self.car3]:
            direction = random.choice(directions)
            new_position = [current_car.x_pos + direction[0], current_car.y_pos + direction[1]]
            current_car.x_pos = new_position[0]
            current_car.y_pos = new_position[1]

            # Ensure the new position is within bounds
            if (0 <= new_position[0] < self.rows) and (0 <= new_position[1] < self.cols):
                x, y = current_car.get_car_coordinates(new_position)
                self.canvas.coords(current_car.the_car, 
                    x - self.car_size, y - self.car_size,
                    x + self.car_size, y + self.car_size
                )
            else:
                print("Invalid Car Position", new_position[0], new_position[1])

        self.root.after(500, self.move_cars_automatically)  # Repeat every 500ms


# Create the main application window
root = tk.Tk()
root.title("Eyantra Robotic Competition - Feeder Weeder")

# Initialize the CarGridApp
app = BuildMainGui(root)

# Calculate car will move in the next time scale.
app.move_cars_automatically()

# Start the main event loop
root.mainloop()
