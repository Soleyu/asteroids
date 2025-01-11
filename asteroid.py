import circleshape
from constants import *
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def split(self):        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(split_angle)
        vector_2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_x_1 = self.position.x #+ (vector_1.x * 0.1)
        new_x_2 = self.position.x #+ (vector_2.x * 0.1)
        new_y_1 = self.position.y #+ (vector_1.y * 0.1)
        new_y_2 = self.position.y #+ (vector_2.y * 0.1)
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector_1 * 1.2
        new_asteroid_2.velocity = vector_2 * 1.2

        
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        