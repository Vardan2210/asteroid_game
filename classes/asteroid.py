import pygame
import random
from .circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x,y, radius)

    def draw(self,screen: pygame.surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event('asteroid_split')
        angle = random.uniform(20, 50)
        first_angle = self.velocity.rotate(angle)
        second_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        first_a = Asteroid(self.position.x, self.position.y, new_radius)
        second_a = Asteroid(self.position.x, self.position.y, new_radius)

        first_a.velocity = first_angle * 1.2

        second_a.velocity= second_angle * 1.2

        

        
