class Algorithm():
    def __init__(self, color):
        if color == "red":
            self.data_collection_path = [(1, 1), (1, 5)]
        elif color == "green":
            self.data_collection_path = [(3, 5), (3, 1)]
        elif color == "blue":
            self.data_collection_path = [(5, 1), (5, 5)]
        self.index = -1
        self.execution_path = []
        self.target_pos = None

    def get_target_position(self, system_state):
        current_path = self.data_collection_path if system_state == "DATA_COLLECTION" else self.execution_path
        self.index += 1
        if self.index < len(current_path):
            self.target_pos = current_path[self.index]
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
        elif delta_x > 0 and delta_y > 0:
            return "right_down"
        elif delta_x > 0 and delta_y < 0:
            return "right_up"
        elif delta_x < 0 and delta_y > 0:
            return "left_down"
        elif delta_x < 0 and delta_y < 0:
            return "left_up"

    def plan_the_path(self, next_target_locations, color, rows, cols, current_x, current_y):
        # Reset the index because the path will change.
        self.index = -1
        current_x = round(current_x)
        current_y = round(current_y)
        for i, box_index in enumerate(next_target_locations):
            x = box_index % rows
            y = box_index // cols
                
            if (x - current_x == 0) or (y - current_y == 0):
                self.execution_path.append((x, y,"Yes"))
            else:
                self.execution_path.append((x, current_y, "No"))
                self.execution_path.append((x, y, "Yes"))
            
            current_x = x
            current_y = y

        # Return home node in the end. Add last node as home node.
        home_x = 0
        home_y = 0
        if color == "red":
            home_x = 0
            home_y = 1
        elif color == "green":
            home_x = 3
            home_y = 6
        elif color == "blue":
            home_x = 6
            home_y = 1

        if current_x != home_x and current_y != home_y:
            self.execution_path.append((home_x, current_y, "No"))
            self.execution_path.append((home_x, home_y, "No"))
        elif (current_x == home_x) ^ (current_y == home_y):
            self.execution_path.append((home_x, home_y, "No"))

        # print(color, "===>", self.execution_path)
        print(color,"->PASS") if (self.execution_path[-1][0] == home_x and self.execution_path[-1][1] == home_y) else print(color,"->FAIL")

    if __name__ == "__main__":
        print("Cannot run this file direclty. Execute gui.py")

