# main.py: ойын циклі
import pygame

from game import Game
from settings import WIDTH, HEIGHT, FONT_PATH


def main(max_frames=None):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Сапёр")
    font = pygame.font.Font(FONT_PATH, 24)
    clock = pygame.time.Clock()
    game = Game()
    running = True
    frame = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game.over:
                    game = Game()
                else:
                    game.handle_key(event.key)
        game.update()
        game.draw(screen, font)
        pygame.display.flip()
        clock.tick(60)
        frame = frame + 1
        if max_frames and frame >= max_frames:
            running = False
    pygame.quit()
    return game


if __name__ == "__main__":
    main()
