from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    num_rows = 12
    num_cols = 16
    cell_size_x = 50
    cell_size_y = 50
    x1 = 50
    y1 = 50

    maze = Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=0)

    maze._break_entrance_and_exit()

    maze.break_walls_r(0, 0)

    maze.reset_cells_visited()

    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()