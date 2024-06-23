import algorithm

class Car(algorithm):
    def __init__(self, root, canvas, rows, cols, cell_size, car_size, x_pos, y_pos, color):
        self.cell_size = cell_size
        self.initial_offset = 30
        # The x_pos rance from 0 to number of cols
        #     y_pos range from 0 to number of rows
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.target_x_pos = x_pos
        self.target_y_pos = y_pos
        self.stride = 0.005
        self.car_head = None

        x, y = self.get_car_coordinates([self.x_pos, self.y_pos])
        self.the_car = canvas.create_rectangle(
            x - car_size, y - car_size,
            x + car_size, y + car_size,
            fill = color
        )

        if color == "red":
            self.car_indx = 1
            self.car_head = "right"
        elif color == "green":
            self.car_indx = 2 
            self.car_head = "left"
        else:
            self.car_indx = 3
            self.car_head = "up"   
        super().__init__(self, color)

    def get_car_coordinates(self, position):
        x = self.initial_offset + position[0] * self.cell_size
        y = self.initial_offset + position[1] * self.cell_size
        return x, y
    
    def is_target_reached(self):
        if (self.x_pos == self.target_x_pos) and (self.y_pos == self.target_y_pos):
            return True
        else:
            return False

    def next_move(self):
        if self.is_target_reached():
            self.target_x_pos, self.target_y_pos = self.get_target_position(self)
            direction = self.get_direction(self.x_pos, self.y_pos, self.target_x_pos, self.target_y_pos)
            
        if self.car_indx == 1:
            # Move this car horizontally right
            self.x_pos += self.stride
        elif self.car_indx == 2:
            # Move this car vertically upward
            self.y_pos -= self.stride
        else:
            # Move this car horizontally left
            self.x_pos -= self.stride

        # There are 3 states the whole system will be in.
        # a) getInformation b) publishData c) startTheWork
        # check which state the system is in. 
        # if a -> move ahead in straight line.
        # if b -> wait and broadcast information.
        # if c -> check position of other cars and take next step.
        # return your next position computed
        # update self.x_pos and self.y_pos

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")

