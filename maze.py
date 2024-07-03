from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        for num in range(0, self.num_cols):
            column = []
            for num in range(0, self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)

        for i in range(0, len(self._cells)):
            for j in range(0, len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell_pos_x = self.cell_size_x * (i) + self.x1
        cell_pos_y = self.cell_size_y * (j) + self.y1
        cell_x2 = cell_pos_x + self.cell_size_x
        cell_y2 = cell_pos_y + self.cell_size_y
        self._cells[i][j].draw(cell_pos_x, cell_pos_y, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        last_column = len(self._cells) - 1
        last_row = len(self._cells[-1]) - 1
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[last_column][last_row]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell.has_bottom_wall = False
        self._draw_cell(last_column, last_row)