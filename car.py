class Car:
    def __init__(self, root, canvas, rows, cols, cell_size, car_size, x_pos, y_pos, color):
        self.cell_size = cell_size
        self.x_pos = x_pos
        self.y_pos = y_pos              
        self.cars = []

        x, y = self.get_car_coordinates([self.x_pos, self.y_pos])
        car = canvas.create_rectangle(
            x - car_size, y - car_size,
            x + car_size, y + car_size,
            fill = color
        )

    def get_car_coordinates(self, position):
        x = position[1] * self.cell_size
        y = position[0] * self.cell_size
        return x, y

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")

