import tkinter as tk
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
        # 5 system states: DATA_COLLECTION, PATH_PLANNING, EXECUTION, STOP
        self.system_state = "DATA_COLLECTION"
        self.total_cars = 3
        self.cars_objects_list = []
        self.car_colors = ["red", "green", "blue"]
        self.gui_plants_data = []
        self.offset = 30

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

    def feeding_or_weeding_the_plants(self, this_car, box_index):
        # Updated the plant status are visited.
        if this_car.car_color != "green":
            self.plants_object.plants_positions[box_index]["STATUS"] = "Feeded"
        else:
            self.plants_object.plants_positions[box_index]["STATUS"] = "Weeded" 

        x = box_index // self.cols
        y = box_index % self.rows

        # feed or weed the box
        action = "weed" if this_car.car_color == "green" else "feed"
        centre_x = self.offset + self.cell_size // 2 + self.cell_size * y 
        centre_y = self.offset + self.cell_size // 2 + self.cell_size * x 
        plant_color = this_car.car_color
        radius = 15
        self.plants_object.feed_weed_the_plant(self.canvas, 
                                                action,
                                                centre_x,
                                                centre_y,
                                                radius, 
                                                plant_color)

    def move_the_car_to_next_coordinate(self, this_car):
        new_position = [this_car.x_pos, this_car.y_pos]

        # Ensure the new position is within bounds
        if (0 <= new_position[0] <= self.rows) and (0 <= new_position[1] <= self.cols):
            x, y = this_car.get_car_coordinates(new_position)
            self.canvas.coords(this_car.the_car, 
                x - this_car.corner_vector[0], y - this_car.corner_vector[1],
                x + this_car.corner_vector[0], y + this_car.corner_vector[1]
            )
        else:
            print("Invalid Car Position", new_position[0], new_position[1],
                "color =", this_car.car_color)

    def scan_four_boxes_around_node(self, this_car):
        boxes_data = []
        for box_row in range(0, 2):
            for box in range(0, 2):
                __row = round(this_car.y_pos)
                __col = round(this_car.x_pos)
                box_index = (__row - 1) * self.cols + (__col - 1) + box + (box_row * self.cols)
                boxes_data.append(self.plants_object.plants_positions[box_index])        
        return boxes_data

    def broadcast_data_to_other_cars(self, plant_data, sensing_car_color):
        for this_car in self.cars_objects_list:
            # This condition checks that we are sending data to other cars 
            if sensing_car_color != this_car.car_color:

                # Send plats data to respective car regarding plants they need to work on after data collection.
                if plant_data["COLOR"] == this_car.car_color:
                    this_car.collected_plants_data.append(plant_data)

    def move_cars_automatically(self):
        # Calculte where to move the car next
        for current_car in self.cars_objects_list:
            current_car.next_move(self.system_state)

        # Move the car on the canvas the gui
        for current_car in self.cars_objects_list:
            if current_car.car_state == "MOVING":
                self.move_the_car_to_next_coordinate(current_car)
                
            elif current_car.car_state == "SENSING":
                # Car will check all the 4 boxes around the node.
                plants_at_node = self.scan_four_boxes_around_node(current_car)
                                    
                for plant_data in plants_at_node:
                    box_index = plant_data["INDEX"]
                    if (0 <= box_index < self.cols * self.rows) and (plant_data["STATUS"] == None):
                        self.plants_object.plants_positions[box_index]["STATUS"] = "Visited"

                        if (plant_data["COLOR"] == current_car.car_color):
                            self.feeding_or_weeding_the_plants(current_car, box_index)

                        elif (plant_data["COLOR"] != "Skip"):
                            # Plant is there in this box but its of different color than current car color
                            self.broadcast_data_to_other_cars(plant_data, current_car.car_color)

            elif current_car.car_state == "FEED_WEED":
                box_index = current_car.execution_path[current_car.index][3]
                self.feeding_or_weeding_the_plants(current_car, box_index)
                
        # Updating the system state
        cars_completed_task = all([current_car.car_state == "STOP" for current_car in self.cars_objects_list])
        if self.system_state == "DATA_COLLECTION" and cars_completed_task:
            print("PATH_PLANNING")
            self.system_state = "PATH_PLANNING"

        cars_completed_task = all([current_car.car_state == "MOVING" for current_car in self.cars_objects_list])
        if self.system_state == "PATH_PLANNING" and cars_completed_task:
            print("EXECUTION")
            self.system_state = "EXECUTION"

        # cars_completed_task = all([current_car.car_state == "STOP" for current_car in self.cars_objects_list])
        # if self.system_state == "PATH_PLANNING" and cars_completed_task:
        #     print("STOP")
        #     self.system_state = "STOP"

        
        self.root.after(10, self.move_cars_automatically)  # Scedule move_cars_automatically every 10ms


# Create the main application window
root = tk.Tk()
root.title("Eyantra Robotics Competition - Feeder Weeder")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x = (screen_width // 2) - (50 + 6 * 100 // 2)
y = (screen_height // 2) - (50 + 6 * 100 // 2)

# Set the geometry of the window. Open window at the centre of screen.
root.geometry(f'{50 + 6 * 100}x{50 + 6 * 100}+{x}+{y}')

# Initialize the CarGridApp
app = BuildMainGui(root)

# Calculate car will move in the next time scale.
app.move_cars_automatically()

# Start the main event loop
root.mainloop()
