import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen,"white", tuple(self.position), self.radius, width=2)
        
    def update(self, dt): #this tells our asteroids to move forward from spawn and to gain speed
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            rock_split = random.uniform(20,50)
            vel1 = self.velocity.rotate(rock_split)
            vel2 = self.velocity.rotate(-rock_split)

            rock1 = Asteroid(self.position.x, self.position.y, new_radius, vel1 * 1.2)
            rock2 = Asteroid(self.position.x, self.position.y, new_radius, vel2 * 1.2)
            return rock1, rock2