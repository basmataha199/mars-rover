import unittest
import io
from contextlib import redirect_stdout
from mars_rover import main

class TestMarsRover(unittest.TestCase):

    def setUp(self):
        self.input_file = "test_input.txt"
    
    def test_case_1(self):
        input_data = """4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF"""
        expected_output = """(4, 4, E)
(0, 4, W) LOST"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        input_data = """4 8
(2, 3, N) FLLFR
(1, 0, S) FFRLF"""
        expected_output = """(2, 3, W)
(1, 0, S) LOST"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_start_edge_move_out_of_bounds(self):
        input_data = """4 8
(4, 8, N) F"""
        expected_output = """(4, 8, N) LOST"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_start_edge_rotate(self):
        input_data = """4 8
(0, 0, S) L"""
        expected_output = """(0, 0, E)"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_empty_commands(self):
        input_data = """4 8
(2, 2, N)"""
        expected_output = """(2, 2, N)"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_navigate_edges(self):
        input_data = """4 8
(0, 0, N) FFFFFFFFRFFFFFFF"""
        expected_output = """(4, 8, E) LOST"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_multiple_rovers(self):
        input_data = """4 8
(2, 3, E) LFRFF
(0, 2, N) FFLFRFF
(4, 4, N) FFRR"""
        expected_output = """(4, 4, E)
(0, 4, W) LOST
(4, 6, S)"""

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_empty_file(self):
        input_data = ""
        expected_output = "Input file is empty."

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)

    def test_no_commands(self):
        input_data = """4 8"""
        expected_output = "No commands found."

        with open(self.input_file, "w") as file:
            file.write(input_data)
        
        f = io.StringIO()
        with redirect_stdout(f):
            main(self.input_file)
        
        output = f.getvalue().strip()
        self.assertEqual(output, expected_output)
        
if __name__ == '__main__':
    unittest.main()
