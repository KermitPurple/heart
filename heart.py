import pygame
import random
from numpy import sin, cos

class Heart:

    selected_color = 1

    def __init__(self, screen, pos = (0,0), scale = 1, size = (100,100)):
        self.screen = screen
        self.pos = pos
        self.scale = scale
        self.size = size
        self.density = self.scale * 10

    def draw(self):
        points = []
        for i in range(2 * self.density):
            theta = i/self.density * 3.14159265
            x = 16 * pow(sin(theta), 3)
            x = int(self.scale * x + self.pos[0])
            y = 13 * cos(theta) - 5 * cos(2 * theta) - 2 * cos(3 * theta) - cos(4 * theta)
            y = -int(self.scale * y - self.pos[1])
            points.append((x,y))
        pygame.draw.polygon(self.screen, self.getcolor(), points)
        pygame.draw.polygon(self.screen, (0,0,0), points, 1)

    def random(self):
        self.pos = (random.randint(0, self.size[0]), random.randint(0, self.size[1]))
        self.scale = random.randint(5,15)
        
    def getcolor(self):
        if Heart.selected_color == 1:
            return (255,0, random.randint(0,150))
        return (255,0, random.randint(0,150))
