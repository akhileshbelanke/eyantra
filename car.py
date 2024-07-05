from algorithm import Algorithm

class Car(Algorithm):
    def __init__(self, root, canvas, rows, cols, cell_size, car_size, x_pos, y_pos, color):
        self.cell_size = cell_size
        self.initial_offset = 30   
        self.x_pos = x_pos # x_pos range from 0 to number of cols
        self.y_pos = y_pos # y_pos range from 0 to number of rows
        self.stride = 0.005
        self.car_head = None
        self.car_length = car_size + 5
        self.car_breadth = car_size
        self.canvas = canvas
        self.corner_vector = [None, None]
        # Car States: MOVING, ON_THE_NODE_REORIENT, SENSING, START and STOP.
        self.car_state = "START"
        self.car_color = color
        self.collected_plants_data = []

        if color == "red":
            self.car_indx = 1
            self.car_head = "right"
            self.target_x_pos = 1
            self.target_y_pos = 1
        elif color == "green":
            self.car_indx = 2 
            self.car_head = "up"
            self.target_x_pos = 3
            self.target_y_pos = 5
        else:
            self.car_indx = 3
            self.car_head = "left"
            self.target_x_pos = 5
            self.target_y_pos = 1

        self.adjust_the_car_facing(self.car_head, caller="init", color=color) 

        super().__init__(color)

    def get_car_coordinates(self, position):
        x = self.initial_offset + position[0] * self.cell_size
        y = self.initial_offset + position[1] * self.cell_size
        return x, y

    def reached_intersection(self):
        if (round(self.x_pos, 3) == round(self.x_pos, 0)) and (round(self.y_pos, 3) == round(self.y_pos, 0)):
            return True
        else:
            return False

    def is_target_reached(self):
        if (round(self.x_pos, 3) == self.target_x_pos) and (round(self.y_pos, 3) == self.target_y_pos):
            return True
        else:
            return False
    
    def check_if_last_node_on_path(self):
        last_element_on_path = len(self.path) - 1
        if (round(self.x_pos) == self.path[last_element_on_path][0]) and (round(self.y_pos) == self.path[last_element_on_path][1]):
            return True
        else:
            return False

    def adjust_the_car_facing(self, car_head, caller, color="yellow"):
        # (left corner point)---> .----------.
        #                         |   car    |
        #                         .----------. <---(right corner point)
        # These two points are required to draw car using create_rectangle api.
        left_corner_x=0
        left_corner_y=0
        right_corner_x=0
        right_corner_y=0

        x, y = self.get_car_coordinates([self.x_pos, self.y_pos])
        # Else part is when car_head is Up/Down
        left_corner_x = x - (self.car_length if (car_head == "left" or car_head == "right") else self.car_breadth)
        left_corner_y = y - (self.car_breadth if (car_head == "left" or car_head == "right") else self.car_length)
        right_corner_x = x + (self.car_length if (car_head == "left" or car_head == "right") else self.car_breadth)
        right_corner_y = y + (self.car_breadth if (car_head == "left" or car_head == "right") else self.car_length)
        self.corner_vector[0] = self.car_length if (car_head == "left" or car_head == "right") else self.car_breadth
        self.corner_vector[1] = self.car_breadth if (car_head == "left" or car_head == "right") else self.car_length

        if caller == "init":
            self.the_car = self.canvas.create_rectangle(
                left_corner_x, left_corner_y,
                right_corner_x, right_corner_y,
                fill = color
                )
        else:
            self.canvas.coords(self.the_car, 
                               left_corner_x, left_corner_y,
                               right_corner_x, right_corner_y
                               )

    def keep_heading_in_same_direction_as_your_are(self):
        # First move the car in required direction
        if self.car_head == "right":
            # Move this car horizontally right
            self.x_pos += self.stride
        elif self.car_head == "up":
            # Move this car vertically upward
            self.y_pos -= self.stride
        elif self.car_head == "left":
            # Move this car horizontally left
            self.x_pos -= self.stride
        elif self.car_head == "down":
            # Move this car vertically downwards
            self.y_pos += self.stride

    def next_move(self, system_state):
        if system_state == "DATA_COLLECTION":
            if self.car_state == "START":
                self.car_state = "MOVING"

            elif self.car_state == "ON_THE_NODE_REORIENT":
                self.target_x_pos, self.target_y_pos = self.get_target_position()
                self.car_head = self.get_direction(self.x_pos, self.y_pos, self.target_x_pos, self.target_y_pos)
                self.adjust_the_car_facing(self.car_head, caller="next_move")
                self.car_state = "MOVING"
                
            elif self.car_state == "MOVING":
                self.keep_heading_in_same_direction_as_your_are()           
                # Then check if it has reached an intersection or not.
                if self.reached_intersection():
                    self.car_state = "SENSING"
                else:
                    self.car_state = "MOVING"

            elif self.car_state == "SENSING":
                if self.is_target_reached():
                    if self.check_if_last_node_on_path():
                        self.car_state = "STOP"
                        print("\n\n", self.collected_plants_data)
                    else:
                        self.car_state = "ON_THE_NODE_REORIENT"
                else:
                    self.car_state = "MOVING"

            elif self.car_state == "STOP":
                pass
        
        elif system_state == "PATH_PLANNING":
            pass
        elif system_state == "EXECUTION":
            pass
        elif system_state == "STOP":
            pass

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")

