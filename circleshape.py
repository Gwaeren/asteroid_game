import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return distance <= (self.radius + other.radius)

    def wrap_around(self):
        # X-axis wrap
        if self.position.x + self.radius < 0:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x - self.radius > SCREEN_WIDTH:
            self.position.x = -self.radius
        # Y-axis wrap
        if self.position.y + self.radius < GAME_TOP_BOUNDARY:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y - self.radius > SCREEN_HEIGHT:
            self.position.y = GAME_TOP_BOUNDARY - self.radius

    def is_off_screen(self):
        return (
            self.position.x + self.radius < 0 or
            self.position.x - self.radius > SCREEN_WIDTH or
            self.position.y + self.radius < GAME_TOP_BOUNDARY or
            self.position.y - self.radius > SCREEN_HEIGHT
        )
