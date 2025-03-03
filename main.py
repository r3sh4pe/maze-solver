from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    num_rows = 3
    num_cols = 3
    cell_size_x = 100
    cell_size_y = 100
    x1 = 50
    y1 = 50

    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze._break_entrance_and_exit()

    maze.cells[1][0].has_bottom_wall = False

    maze.cells[1][1].has_top_wall = False
    maze.cells[1][1].has_left_wall = False

    maze.cells[0][1].has_right_wall = False

    maze.cells[2][1].has_left_wall = False
    maze.cells[2][1].has_bottom_wall = False

    maze.cells[1][2].has_top_wall = False

    for i in range(num_cols):
        for j in range(num_rows):
            maze.cells[i][j].draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()