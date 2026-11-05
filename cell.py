# cell.py


class Cell:
    """Одна клетка поля."""

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.has_mine = False
        self.is_open = False
        self.count = 0  # сколько мин вокруг

    def open(self):
        self.is_open = True

    def symbol(self, show_mines):
        if self.is_open:
            if self.has_mine:
                return "*"
            return str(self.count)
        if show_mines and self.has_mine:
            return "*"
        return "#"
