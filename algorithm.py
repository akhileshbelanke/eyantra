import math
import itertools

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
    
    def get_closest_next_node_to_current_node(self, x, y, current_x, current_y):
        targets = [(x, y), (x+1, y), (x, y+1), (x+1, y+1)]
        minimum_distance = []
        for target_node in targets:
            dist = abs(current_x - target_node[0]) + abs(current_y - target_node[1])
            minimum_distance.append(dist)
        index = minimum_distance.index(min(minimum_distance)) 
        return targets[index][0], targets[index][1]
    
    def bellman_held_karp_algorithm(self, dist, start, end):
        n = len(dist)
        # If there is no color found for that car, just return to home from
        # current location. Thus returing start and end point.
        if n == 2:
            return dist[0][1], [start, end]
        
        # Initialize the memoization table and path tracking
        dp = {}
        path = {}

        # Set initial distances for direct paths from start
        for i in range(n):
            if i != start:
                dp[(1 << start) | (1 << i), i] = dist[start][i]
                path[(1 << start) | (1 << i), i] = [start, i]

        # Iterate over sets of increasing length
        for subset_size in range(3, n + 1):
            for subset in itertools.combinations(range(n), subset_size):
                if start not in subset or end in subset:
                    continue
                bits = 0
                for bit in subset:
                    bits |= 1 << bit

                for k in subset:
                    if k == start or k == end:
                        continue
                    prev_bits = bits & ~(1 << k)
                    
                    min_cost = float('inf')
                    best_prev = None
                    for m in subset:
                        if m == start or m == k:
                            continue
                        cost = dp[(prev_bits, m)] + dist[m][k]
                        if cost < min_cost:
                            min_cost = cost
                            best_prev = m

                    dp[(bits, k)] = min_cost
                    path[(bits, k)] = path[(prev_bits, best_prev)] + [k]

        # Final leg from any node to the end node
        bits = (1 << n) - 1
        bits &= ~(1 << end)
        min_cost = float('inf')
        best_k = None

        for k in range(n):
            if k != start and k != end:
                cost = dp[(bits, k)] + dist[k][end]
                if cost < min_cost:
                    min_cost = cost
                    best_k = k

        final_path = path[(bits, best_k)] + [end]

        return min_cost, final_path

    def plan_the_path(self, next_target_locations, color, rows, cols, current_x, current_y):
        # Return home node in the end. Add last node as home node.
        self.index = -1
        current_x = round(current_x)
        current_y = round(current_y)
        home_x = 0 if color == "red" else 3 if color == "green" else 6
        home_y = 1 if color == "red" else 6 if color == "green" else 1

        vectors = [(current_x, current_y), (home_x, home_y)]
        for box_index in next_target_locations[::-1]:
            x = box_index % rows
            y = box_index // cols
            vectors.insert(1, (x, y))

        distance_matrix = []
        for current_node in vectors:
            current_node_list = []
            for target_node in vectors:
                xsqr = (target_node[0] - current_node[0]) ** 2
                ysqr = (target_node[1] - current_node[1]) ** 2
                distance = round(math.sqrt(xsqr + ysqr), 2)
                current_node_list.append(distance)
            distance_matrix.append(current_node_list)

        cost, output_path = self.bellman_held_karp_algorithm(distance_matrix, 0, len(vectors)-1)

        current_x = vectors[0][0]
        current_y = vectors[0][1]
        for i in range(1, len(output_path)):
            x = vectors[output_path[i]][0]
            y = vectors[output_path[i]][1]
            if i < (len(output_path) - 1):
                # print("###")
                newx, newy = self.get_closest_next_node_to_current_node(vectors[output_path[i]][0], vectors[output_path[i]][1], current_x, current_y)
                # print("old->", x, y, "new->", newx, newy)
            else:
                newx = vectors[output_path[i]][0]
                newy = vectors[output_path[i]][1]

            if (newx - current_x == 0) or (newy - current_y == 0):
                if i == (len(output_path) - 1):
                    self.execution_path.append((newx, newy, "No"))
                else:
                    self.execution_path.append((newx, newy, "Yes", y * cols + x))
            else:
                self.execution_path.append((newx, current_y, "No"))
                if i == (len(output_path) - 1):
                    self.execution_path.append((newx, newy, "No"))
                else:
                    self.execution_path.append((newx, newy, "Yes", y * cols + x))

            current_x = newx
            current_y = newy

        print("exepath", color, output_path, self.execution_path)

if __name__ == "__main__":
    print("Cannot run this file direclty. Execute gui.py")

