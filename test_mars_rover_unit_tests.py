import unittest
from unittest.mock import patch, mock_open
from mars_rover import MarsRover, process_rover, main

class TestMarsRover(unittest.TestCase):

    def test_set_position(self):
        rover = MarsRover("4 8")
        rover.set_position(2, 3, 'N')
        self.assertEqual(rover.position, (2, 3))
        self.assertEqual(rover.orientation, 'N')

    def test_rotate_left(self):
        rover = MarsRover("4 8")
        rover.set_position(0, 0, 'N')
        rover.rotate('L')
        self.assertEqual(rover.orientation, 'W')

    def test_rotate_right(self):
        rover = MarsRover("4 8")
        rover.set_position(0, 0, 'N')
        rover.rotate('R')
        self.assertEqual(rover.orientation, 'E')

    def test_move_forward(self):
        rover = MarsRover("4 8")
        rover.set_position(0, 0, 'N')
        rover.move_forward()
        self.assertEqual(rover.position, (0, 1))

    def test_move_forward_off_grid(self):
        rover = MarsRover("4 8")
        rover.set_position(4, 8, 'N')
        rover.move_forward()
        self.assertTrue(rover.is_lost)
        self.assertEqual(rover.get_state(), "(4, 8, N) LOST")

    def test_process_commands(self):
        rover = MarsRover("4 8")
        rover.set_position(2, 3, 'E')
        result = rover.process_commands('LFRFF')
        self.assertEqual(result, "(4, 4, E)")


if __name__ == '__main__':
    unittest.main()
