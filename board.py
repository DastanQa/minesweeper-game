# board.py: алаңды жасайды, миналарды қояды, ұяшықтарды құрады
import random

from mine_cell import MineCell
from safe_cell import SafeCell
from settings import SIZE, MINES


class Board:
    def __init__(self):
        self.map = []
        for r in range(SIZE):
            line = []
            for c in range(SIZE):
                line.append(False)
            self.map.append(line)
        self.place_mines()
        self.cells = self.build_cells()

    def place_mines(self):
        placed = 0
        while placed < MINES:
            r = random.randint(0, SIZE - 1)
            c = random.randint(0, SIZE - 1)
            if not self.map[r][c]:
                self.map[r][c] = True
                placed = placed + 1

    def count_near(self, row, col):
        total = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                r = row + dr
                c = col + dc
                if r >= 0 and r < SIZE and c >= 0 and c < SIZE and self.map[r][c]:
                    total = total + 1
        return total

    def build_cells(self):
        cells = []
        for r in range(SIZE):
            for c in range(SIZE):
                if self.map[r][c]:
                    cells.append(MineCell(r, c))
                else:
                    cells.append(SafeCell(r, c, self.count_near(r, c)))
        return cells
