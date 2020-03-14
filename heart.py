import pygame
from numpy import sin, cos

class Heart:
    def __init__(self, screen, pos, scale, density):
        self.screen = screen
        self.pos = pos
        self.scale = scale
        self.density = density

    def draw(self):
        for i in range(2 * self.density):
            theta = i/self.density * 3.14159265
            x = 16 * pow(sin(theta), 3)
            x = int(self.scale * x + self.pos[0])
            y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
            y = -int(self.scale * y - self.pos[1])
            pygame.draw.circle(self.screen, (255,255,255), (x,y), 3)

