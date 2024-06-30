# Mars Rover Problem
This repository contains a solution to the Mars Rover problem, where robots navigate a grid on Mars based on a series of commands.

## Problem Description
The world is modeled as a grid with size m x n. Each robot has a position (x, y) and an orientation (N, E, S, W). Robots can move forward one space (F), rotate left by 90 degrees (L), or rotate right by 90 degrees (R). If a robot moves off the grid, it is marked as 'lost' and its last valid grid position and orientation is recorded.

### Input Format
The input consists of the grid size followed by the initial state and commands for each robot. For example:


```
4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF
```

### Output Format
The output is the final position and orientation of the robots. If a robot is lost, it is marked as 'LOST'. For example:
```
4, 4, E
0, 4, W LOST
```

## How the Program Works
### Initialization
1. MarsRover Class:
- The MarsRover class is initialized with the grid size, which is specified as a tuple (m, n).
- The rover's initial position (x, y) and orientation (N, E, S, W) are set using the set_position method.

### Command Processing
2. Commands:
- The rover's movement is controlled by the process_commands method, which processes a series of commands (L, R, F).
- Rotation Commands:
'L' (Left): Rotate the rover 90 degrees to the left.
'R' (Right): Rotate the rover 90 degrees to the right.
- Forward Command:
'F' (Forward): Move the rover one step forward in the direction it is currently facing.

### Boundary Checks
3. Boundary Checking:
- If the rover moves off the grid, it is marked as 'lost' and its last valid position and orientation are recorded. The rover stops processing further commands if it is lost.

### Input and Output
4. Input:

- The program reads the input from a file, which includes the grid size and the initial state and commands for each rover.
The input is split and parsed to extract the grid size and each rover's initial state and commands.
5. Output:

- The program processes each rover's commands and prints the final state of each rover, including whether any rover is lost.

### Example
For the input:
```
4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF
```

The output would be:
```
4, 4, E
0, 4, W LOST
```

## How to Run the Program
1. Save the program in a file named mars_rover.py.
2. Create an input file (e.g., input.txt) with the grid size and commands in the specified format.
3. Open a terminal or command prompt and navigate to the directory where mars_rover.py and input.txt are saved.
4. Run the program:


```
python mars_rover.py input.txt
```

## Running the Tests
1. Save the test functions in a file named test_mars_rover.py.
2. Open a terminal or command prompt and navigate to the directory where test_mars_rover.py is saved.
3. Run the tests:

```
python -m unittest test_mars_rover.py
```
### Unit Tests
The unit tests check individual methods of the MarsRover class to ensure they work as expected. The tests cover setting position, rotating, moving forward, handling boundary conditions, and processing commands.

### Integration Tests
The integration tests check reading operations and capture print statements to verify the overall behavior of the main function by comparing the actual output to the expected output. It also includes more edge cases to test the overall behavior.

## Future Enhancements
### Scaling for Production Use
To safely scale this solution for production use, consider the following enhancements:

1. Distributed Computing:

- Implement the solution as a distributed system using multiple instances of a service, to process large numbers of rovers in parallel.
- Distribute the processing of different rovers across multiple nodes to handle large-scale deployments efficiently.

2. Concurrent Processing:

- Use concurrent processing (e.g., multiprocessing or multithreading) to process multiple rovers simultaneously within a single machine.
- Utilize Python's `concurrent.futures.ThreadPoolExecutor` or `multiprocessing.Pool` as we did for this solution for efficient parallel execution.

3. Cloud Infrastructure:

- Utilize cloud-based storage solutions like Amazon S3 or Google Cloud Storage for input and output data.

4. Load Balancing:

- Implement load balancing to distribute the computational load evenly across available resources, ensuring efficient utilization and avoiding bottlenecks.

5. Efficient Data Management:

- Optimize file reading and writing operations to handle large input and output files efficiently.
- Consider using streaming techniques to process data in chunks, reducing memory usage and improving performance.

### Input and Output Handling
- Although the current implementation uses input files for simplicity, and prints in StdOut the program can be adapted to accept input via RPC (Remote Procedure Call) or HTTP requests. This would be more suitable for real-time applications and distributed systems where commands for rovers are received dynamically.

- For example, a web API could be developed to receive rover commands as HTTP requests and process them accordingly, returning the final states as HTTP responses.