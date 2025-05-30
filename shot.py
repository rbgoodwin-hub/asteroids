import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

class Bomb(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, BOMB_RADIUS)

    def draw(self, screen):
        rect_pos = (100, 100)
        rect_size = (200, 150)
        rect = pygame.Rect(rect_pos, rect_size)
        pygame.draw.rect(screen, "black", rect, 0) 
        pygame.draw.ellipse(screen, "purple", rect,  width=4)

    def update(self, dt):
        self.position += self.velocity * -dt