import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_different_dimensions(self):
        num_cols = 5
        num_rows = 8
        m2 = Maze(10, 10, num_rows, num_cols, 20, 15)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )

    def test_maze_cell_initialization(self):
        num_cols = 3
        num_rows = 3
        m3 = Maze(5, 5, num_rows, num_cols, 30, 30)
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m3._cells[i][j]
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)

    def test_break_entrance_and_exit(self):
        num_cols = 3
        num_rows = 3
        m4 = Maze(5, 5, num_rows, num_cols, 30, 30)

        self.assertTrue(m4._cells[0][0].has_top_wall)
        self.assertTrue(m4._cells[num_cols - 1][num_rows - 1].has_bottom_wall)

        m4._break_entrance_and_exit()

        self.assertFalse(m4._cells[0][0].has_top_wall)
        self.assertFalse(m4._cells[num_cols - 1][num_rows - 1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()