# game_object.py: ата-ана класы. Алаңдағы барлық объектіге (ұяшық, курсор) ортақ
import pygame

from settings import LEFT, TOP, CELL


class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, row, col):
        super().__init__()
        self.image = image
        self.row = row
        self.col = col
        self.rect = self.image.get_rect()
        self.set_place(row, col)

    def set_place(self, row, col):
        # объектіні алаңның керек қатары мен бағанына қояды
        self.row = row
        self.col = col
        self.rect.topleft = (LEFT + col * CELL, TOP + row * CELL)

    def update(self):
        # еншілес кластар қайта анықтайды (анимация)
        pass
