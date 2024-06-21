class Car:
    def __init__(self, root, canvas, rows, cols, cell_size, car_size, x_pos, y_pos, color):
        self.cell_size = cell_size
        # The x_pos rance from 0 to number of cols
        #     y_pos range from 0 to number of rows
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.stride = 0.005              

        x, y = self.get_car_coordinates([self.x_pos, self.y_pos])
        self.the_car = canvas.create_rectangle(
            x - car_size, y - car_size,
            x + car_size, y + car_size,
            fill = color
        )
        
        if color == "red":
            self.car_indx = 1
        elif color == "green":
            self.car_indx = 2 
        else:
            self.car_indx = 3

    def get_car_coordinates(self, position):
        x = position[1] * self.cell_size
        y = position[0] * self.cell_size
        return x, y
    
    def next_move(self):
        # There are 3 states the whole system will be in.
        # a) getInformation b) publishData c) startTheWork
        # check which state the system is in. 
        # if a -> move ahead in straight line.
        # if b -> wait and broadcast information.
        # if c -> check position of other cars and take next step.
        # return your next position computed
        # update self.x_pos and self.y_pos
        pass

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")

