class Car:
    def __init__(self, root, canvas, rows, cols, cell_size, car_size):
        self.cell_size = cell_size

        # Initial positions of the cars
        self.car_data = {
            "car_initial_position": [[1, 0], [1, cols], [rows, cols-3]],
            "car_color"           : ["blue", "red", "green"],   
        }        
        
        self.car_positions = self.car_data["car_initial_position"]
        self.cars = []

        for car_index in range(0, 3):
            x, y = self.get_car_coordinates(self.car_data["car_initial_position"][car_index])
            car = canvas.create_rectangle(
                x - car_size, y - car_size,
                x + car_size, y + car_size,
                fill=self.car_data["car_color"][car_index]
            )
            self.cars.append(car)

    def get_car_coordinates(self, position):
        x = position[1] * self.cell_size
        y = position[0] * self.cell_size
        return x, y

if __name__ == "__main__":
    print("Cannot run directly this file. Execute gui.py")

