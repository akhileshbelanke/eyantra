This is eyantra robotics competition 2018 project.

This is simulator to develop and verify the working of path planning algorithm for robots to manuever on the grid.

Project Tasks:
Done - Implement opening tikinter, drawing grid, drawing circles.
Done - Implement drawing car.
Done - Implement moving single car in straight line path.
Done - Defining classes - gui, car, plant and algorithm.
Done - Implement adjust car facing, car head and reorientation logic.
Done - Implement moving cars on a fixed path.
Done - Defining state machine for car.
Done - Implement moving cars on fixed path as per the state machine.
Done - Add plants randomly to the grid.
Done - Implement sensing logic to sense which plant is placed in the four squares around the node.
Done - Collect all the sensed data in that paricular car object.
Done - Feed or Weed the plants on the fixed path as per appropriate color.
Done - Data collection and logging.
Done - Data broadcasting mechanism immediatly as the car finds the plant of other car.
       - Modified data logging mechanism to broadcast/collect data of plants which are not feeded/weeded by the sensing car.
Done - Implement path as you get the information of where are the appropriate plants located in the grid - path planning shortest path algorithm.
       Done - Add System states - dataCollection, pathPlanning, Execution, Stop. 
       Done - keep two different paths static and dynamic - static path for data collection and dynamic path for execution.
       Done - Update dynamic path according to algorithm.
       Done - Move on this path.
Todo - Obstacle avoidance algorithm.
Todo - Adding appropriate delays - sensing, feeding, weeding, and turning.
