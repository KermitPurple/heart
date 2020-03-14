import pygame
import os
from heart import Heart
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 600,600
screen = pygame.display.set_mode(size)
heart = Heart(screen, (size[0]/2, size[1]/2), 10, size)
heart.random()
running = True
pygame.key.set_repeat(40)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0,0,0))
        heart.draw()
        pygame.display.update()
