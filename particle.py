# particle.py: визуалды әсер. Ұсақ бөлшек шашырап, өзін өзі жояды
import random

import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, center, color):
        super().__init__()
        size = random.randint(3, 6)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=center)
        self.dx = random.randint(-4, 4)
        self.dy = random.randint(-6, -1)
        self.life = 30

    def move(self):
        self.rect.x = self.rect.x + self.dx
        self.rect.y = self.rect.y + self.dy
        self.dy = self.dy + 1  # төмен тартылады

    def age(self):
        self.life = self.life - 1
        if self.life <= 0:
            self.kill()

    def update(self):
        self.move()
        self.age()
