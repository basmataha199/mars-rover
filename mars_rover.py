from concurrent.futures import ThreadPoolExecutor

class MarsRover:
    """
    Represents a Mars Rover that can navigate on a grid.
    """

    def __init__(self, grid_size):
        """
        Initializes a MarsRover object.

        Args:
            grid_size (str): The size of the grid in the format "x y".

        Attributes:
            grid_x (int): The size of the grid in the x-axis.
            grid_y (int): The size of the grid in the y-axis.
            orientations (list): The possible orientations of the rover.
            orientation_changes (dict): The changes in orientation based on the commands.
            moves (dict): The movements in each orientation.
            position (tuple): The current position of the rover.
            orientation (str): The current orientation of the rover.
            is_lost (bool): Indicates if the rover is lost.
        """
        self.grid_x, self.grid_y = map(int, grid_size.split())
        self.orientations = ['N', 'E', 'S', 'W']
        self.orientation_changes = {
            'L': -1,
            'R': 1
        }
        self.moves = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0)
        }
        self.position = None
        self.orientation = None
        self.is_lost = False

    def set_position(self, x, y, orientation):
        """
        Sets the position and orientation of the rover.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.
            orientation (str): The orientation of the rover.
        """
        self.position = (int(x), int(y))
        self.orientation = orientation
        self.is_lost = False

    def process_commands(self, commands):
        """
        Processes a list of commands and moves the rover accordingly.

        Args:
            commands (list): A list of commands to be executed.

        Returns:
            str: The current state of the rover in the format "x, y, orientation" or "x, y, orientation LOST".
        """
        for command in commands:
            if command in self.orientation_changes:
                self.rotate(command)
            elif command == 'F':
                self.move_forward()
            if self.is_lost:
                break
        return self.get_state()

    def rotate(self, direction):
        """
        Rotates the rover in the specified direction.

        Args:
            direction (str): The direction to rotate the rover. Can be 'L' (left) or 'R' (right).
        """
        current_index = self.orientations.index(self.orientation)
        new_index = (current_index + self.orientation_changes[direction]) % 4
        self.orientation = self.orientations[new_index]

    def move_forward(self):
        """
        Moves the rover one step forward in its current orientation.
        If the rover goes out of bounds, it is considered lost.
        """
        move_x, move_y = self.moves[self.orientation]
        new_x = self.position[0] + move_x
        new_y = self.position[1] + move_y

        if 0 <= new_x <= self.grid_x and 0 <= new_y <= self.grid_y:
            self.position = (new_x, new_y)
        else:
            self.is_lost = True

    def get_state(self):
        """
        Returns the current state of the rover.

        Returns:
            str: The current state of the rover in the format "x, y, orientation" or "x, y, orientation LOST".
        """
        state = f"({self.position[0]}, {self.position[1]}, {self.orientation})"
        if self.is_lost:
            state += " LOST"
        return state

def process_rover(grid_size, initial_state, commands):
    """
    Process the commands for a Mars Rover.

    Args:
        grid_size (str): The size of the grid in the format 'x y'.
        initial_state (str): The initial state of the rover in the format 'x, y, orientation'.
        commands (str): The commands to be executed by the rover.

    Returns:
        str: The final state of the rover after executing the commands.

    """
    x, y, orientation = initial_state.split(', ')
    rover = MarsRover(grid_size)
    rover.set_position(x, y, orientation)
    result = rover.process_commands(commands.strip())
    return result

def main(input_file):
    """
    Process the input file and execute tasks in parallel using ThreadPoolExecutor.

    Args:
        input_file (str): The path to the input file.

    Returns:
        None
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    if not lines:
        print("Input file is empty.")
        return
    
    grid_size = lines[0].strip()
    tasks = []

    if len(lines) == 1:
        print("No commands found.")
        return

    with ThreadPoolExecutor() as executor:
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.split(') ')
            if len(parts) == 1:
                initial_state = parts[0].strip('(').strip(')')
                commands = ""
            else:
                initial_state, commands = parts
                initial_state = initial_state.strip('(')
            
            task = executor.submit(process_rover, grid_size, initial_state, commands)
            tasks.append(task)

        for task in tasks:
            print(task.result())

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mars_rover.py <input_file>")
    else:
        input_file = sys.argv[1]
        main(input_file)
