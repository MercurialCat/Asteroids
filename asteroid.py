import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", tuple(self.position), self.radius, width=2)
        
    def update(self, dt): #this tells our asteroids to move forward from spawn and to gain speed
        self.position += (self.velocity * dt)
            
            