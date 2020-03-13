import pygame
import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "15,30"

pygame.display.init()
size = 600,600
screen = pygame.display.set_mode(size)
running = True
pygame.key.set_repeat(40)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (255,255,255), (int(size[0]/2), int(size[1]/2)), 20)
        pygame.display.update()
