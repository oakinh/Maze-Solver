from cell import Cell
import time
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed
        if self.seed:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        directions = [
        (0, 1),  # down
        (0, -1), # up
        (1, 0),  # right
        (-1, 0)  # left
        ]
        while True:
            available_indexes = []

            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]

                if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                    if not self._cells[ni][nj].visited:
                        available_indexes.append((ni, nj))

            if not available_indexes:
                self._draw_cell(i, j)
                return
            
            direction_to_move = random.choice(available_indexes)
            next_cell = self._cells[direction_to_move[0]][direction_to_move[1]]

            if i < direction_to_move[0]:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif i > direction_to_move[0]:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif j < direction_to_move[1]:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif j > direction_to_move[1]:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            
            self._break_walls_r(direction_to_move[0], direction_to_move[1])

    

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        if self._solve_r(0, 0) == True:
            return True
        else:
            return False

    def _solve_r(self, i, j):
            
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            return True
        
        directions = [
        (0, 1, "has_bottom_wall"),  # down
        (0, -1, "has_top_wall"), # up
        (1, 0, "has_right_wall"),  # right
        (-1, 0, "has_left_wall")  # left
        ]
        
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]

            if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                next_cell = self._cells[ni][nj]
                attribute_wall_exists = getattr(current_cell, direction[2])
                # attribute_adjacent_wall_exists = getattr(next_cell, direction[3])
                if not next_cell.visited and not attribute_wall_exists:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(ni, nj) == True:
                        return True
                    else:
                        current_cell.draw_move(next_cell, undo=True)
        return False

            





            

            

            

