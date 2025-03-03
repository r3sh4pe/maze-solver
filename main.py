from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)

    # Create a 3x3 grid of cells
    cell_size = 100
    cells = []

    for x in range(3):
        for y in range(3):
            # Calculate cell coordinates
            x1 = 50 + x * cell_size
            y1 = 50 + y * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Create cell with different wall configurations
            cell = Cell(x1, y1, x2, y2, win)

            # Customize some cells (examples)
            if x == 1 and y == 0:  # Middle top cell
                cell.has_bottom_wall = False
            if x == 1 and y == 1:  # Center cell
                cell.has_top_wall = False
                cell.has_left_wall = False
            if x == 0 and y == 1:  # Left middle cell
                cell.has_right_wall = False
            if x == 2 and y == 1:  # Right middle cell
                cell.has_left_wall = False
                cell.has_bottom_wall = False
            if x == 1 and y == 2:  # Bottom middle cell
                cell.has_top_wall = False

            cells.append(cell)

    # Draw all cells
    for cell in cells:
        cell.draw()

    win.wait_for_close()


if __name__ == "__main__":
    main()