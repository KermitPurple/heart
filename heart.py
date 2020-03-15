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
        elif Heart.selected_color == 2:
            return random.choice([(255,0,0),(255,90,0), (255,230,0), (43, 255, 0), (0,255,255), (0,0,255), (140,0,255),(225,0,255)])
        elif Heart.selected_color == 3:
            return random.choice([(206,0,103), (156,51,156), (0,51,153)])
        elif Heart.selected_color == 4:
            return random.choice([(255, 33, 142), (255,214,0), (33,176,254)])
        elif Heart.selected_color == 5:
            return random.choice([(90, 207, 250), (245, 171, 186), (255,255,255)])
        elif Heart.selected_color == 6:
            color = pygame.Color(255)
            color.hsva = (random.randint(1,350),100,100)
            return color

        return (255,0, random.randint(0,150))
