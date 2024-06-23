class Algorithm():
    def __init__(self, color):
        if color == "red":
            self.path = [(1, 1), (5, 1), (5, 5), (1, 5), (1, 1), (0, 1)]
        elif color == "green":
            self.path = [(1, 1), (5, 1), (5, 5), (1, 5), (1, 1), (0, 1)]
        else:
            self.path = [(1, 1), (5, 1), (5, 5), (1, 5), (1, 1), (0, 1)]
        self.index = 0
        self.target_pos = None

    def get_target_position(self):
        self.target_pos = self.path[self.index]
        self.index += 1
        return self.target_pos[0], self.target_pos[1]
    
    def get_direction(self, current_x, current_y, target_x, target_y):
        # This algorithm is assuming that list of points in the path list will be in line of sight.
        # If the line of sight changes, then the next point will be next point in the list.
        delta_x = target_x - current_x
        delta_y = target_y - current_y
        # Directions are up, down, left and right.
        if delta_x > 0 and delta_y == 0:
            return "right"
        elif delta_x < 0 and delta_y == 0:
            return "left"
        elif delta_x == 0 and delta_y < 0:
            return "up"
        elif delta_x == 0 and delta_y > 0:
            return "down"
        else:
            print("Incorrect Target Direction")

    if __name__ == "__main__":
        print("Cannot run this file direclty. Execute gui.py")

