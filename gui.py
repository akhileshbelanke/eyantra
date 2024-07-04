import tkinter as tk
import random
import car
import grid
import plants

class BuildMainGui():
    def __init__(self, root, rows=6, cols=6, cell_size=100, car_size=10, num_cars=3):
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.car_size = car_size
        self.root = root
        self.canvas = tk.Canvas(root, width=50+cols * cell_size, height=50+rows * cell_size, bg="white")
        self.canvas.pack()
        # 5 system states: DATA_COLLECTION, DATA_XCHANGE, CALC_PATH, EXEC, DONE
        self.system_state = "DATA_COLLECTION"
        self.total_cars = 3
        self.cars_objects_list = []
        self.car_colors = ["red", "green", "blue"]
        self.gui_plants_data = []

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
            if current_car.car_state == "MOVING":
                new_position = [current_car.x_pos, current_car.y_pos]

                # Ensure the new position is within bounds
                if (0 <= new_position[0] <= self.rows) and (0 <= new_position[1] <= self.cols):
                    x, y = current_car.get_car_coordinates(new_position)
                    self.canvas.coords(current_car.the_car, 
                        x - current_car.corner_vector[0], y - current_car.corner_vector[1],
                        x + current_car.corner_vector[0], y + current_car.corner_vector[1]
                    )
                else:
                    print("Invalid Car Position", new_position[0], new_position[1],
                        "color =", current_car.car_color)
            elif current_car.car_state == "SENSING":
                # The car is not moving here. The only updating the data structures.
                # Car will check all the 4 boxes around the node.
                for box_row in range(0, 2):
                    for box in range(0, 2):
                        __row = round(current_car.y_pos)
                        __col = round(current_car.x_pos)
                        box_index = (__row - 1) * self.cols + (__col - 1) + box + (box_row * self.cols)
                        plant_data = self.plants_object.plants_positions[box_index]

                        if (0 <= box_index < self.cols * self.rows) and (plant_data["STATUS"] == None):
                            
                            self.plants_object.plants_positions[box_index]["STATUS"] = "Visited"

                            if (plant_data["COLOR"] == current_car.car_color):
                                # Updated the plant status are visited.
                                if current_car.car_color != "green":
                                    self.plants_object.plants_positions[box_index]["STATUS"] = "Feeded"
                                else:
                                    self.plants_object.plants_positions[box_index]["STATUS"] = "Weeded" 

                                # feed or weed the box
                                action = "weed" if current_car.car_color == "green" else "feed"
                                centre_x = self.cell_size * (current_car.x_pos + box) - self.cell_size // 2
                                centre_y = self.cell_size * (current_car.y_pos + box_row) - self.cell_size // 2
                                plant_color = current_car.car_color
                                radius = 15
                                self.plants_object.feed_weed_the_plant(self.canvas, 
                                                                       action,
                                                                       centre_x,
                                                                       centre_y,
                                                                       radius, 
                                                                       plant_color)
                            elif (plant_data["COLOR"] != "Skip"):
                                # Plant is there in this box but its of different color than current car color
                                self.broadcast_data_to_other_cars(plant_data, current_car.car_color)
                                pass
                
        self.root.after(10, self.move_cars_automatically)  # Scedule move_cars_automatically every 10ms

    def broadcast_data_to_other_cars(self, plant_data, sensing_car_color):
        for this_car in self.cars_objects_list:
            # This condition checks that we are sending data to other cars 
            if sensing_car_color != this_car.car_color:

                # Send plats data to respective car regarding plants they need to work on after data collection.
                if plant_data["COLOR"] == this_car.car_color:
                    this_car.collected_plants_data.append(plant_data)


# Create the main application window
root = tk.Tk()
root.title("Eyantra Robotic Competition - Feeder Weeder")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x = (screen_width // 2) - (50 + 6 * 100 // 2)
y = (screen_height // 2) - (50 + 6 * 100 // 2)

# Set the geometry of the window
root.geometry(f'{50 + 6 * 100}x{50 + 6 * 100}+{x}+{y}')

# Initialize the CarGridApp
app = BuildMainGui(root)

# Calculate car will move in the next time scale.
app.move_cars_automatically()

# Start the main event loop
root.mainloop()
