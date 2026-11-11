# timer.py: ойын уақытын кадр санауышымен санайды
class Timer:
    def __init__(self):
        self.ticks = 0

    def update(self):
        self.ticks = self.ticks + 1

    def seconds(self):
        return self.ticks // 60
