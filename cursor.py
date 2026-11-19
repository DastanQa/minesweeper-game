# cursor.py: таңдалған ұяшықты көрсететін жақтау (ойыншының объектісі)
import pygame

from game_object import GameObject
from settings import SIZE, CELL, load_image


class Cursor(GameObject):
    def __init__(self):
        self.frames = []
        for i in range(2):
            self.frames.append(load_image(f"cursor_{i}.png", (CELL - 2, CELL - 2)))
        super().__init__(self.frames[0], 0, 0)
        self.frame = 0
        self.last_switch = pygame.time.get_ticks()

    def move(self, key):
        if key == pygame.K_UP and self.row > 0:
            self.set_place(self.row - 1, self.col)
        if key == pygame.K_DOWN and self.row < SIZE - 1:
            self.set_place(self.row + 1, self.col)
        if key == pygame.K_LEFT and self.col > 0:
            self.set_place(self.row, self.col - 1)
        if key == pygame.K_RIGHT and self.col < SIZE - 1:
            self.set_place(self.row, self.col + 1)

    def find_cell(self, cells):
        # курсор тұрған ұяшықты соқтығысу арқылы табады
        hits = pygame.sprite.spritecollide(self, cells, False)
        return hits[0]

    def update(self):
        # жақтау жыпылықтайды: екі кадр кезекпен ауысады
        now = pygame.time.get_ticks()
        if now - self.last_switch > 350:
            self.frame = (self.frame + 1) % len(self.frames)
            self.image = self.frames[self.frame]
            self.last_switch = now
