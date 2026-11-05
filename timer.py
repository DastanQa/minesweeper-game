# timer.py
import time


class Timer:
    """Секундомер."""

    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def elapsed(self):
        return int(time.time() - self.start_time)
