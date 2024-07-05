class Algorithm():
    def __init__(self, color):
        if color == "red":
            self.data_collection_path = [(1, 1), (1, 5)]
        elif color == "green":
            self.data_collection_path = [(3, 5), (3, 1)]
        elif color == "blue":
            self.data_collection_path = [(5, 1), (5, 5)]
        self.index = 0
        self.execution_path = []
        self.target_pos = None

    def get_target_position(self, system_state):
        current_path = self.data_collection_path if system_state == "DATA_COLLECTION" else self.execution_path
        if self.index < len(current_path):
            self.target_pos = current_path[self.index]
        self.index += 1
        return self.target_pos[0], self.target_pos[1]
    
    def get_direction(self, current_x, current_y, target_x, target_y):
        # This algorithm is assuming that list of points in the path list will be in line of sight.
        # If the line of sight changes, then the next point will be next point in the list.
        delta_x = round(target_x - current_x, 1)
        delta_y = round(target_y - current_y, 1)
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

    def plan_the_path(self, next_target_locations, color, rows, cols):
        # Reset the index because the path will change.
        self.index = 0
        for box_index in next_target_locations:
            x = box_index % rows
            y = box_index // cols
            self.execution_path.append((x, y))
        
        # Return home node.
        if color == "red":
            self.execution_path.append((0, 1))
        elif color == "green":
            self.execution_path.append((3, 6))
        elif color == "blue":
            self.execution_path.append((6, 1))

    if __name__ == "__main__":
        print("Cannot run this file direclty. Execute gui.py")

