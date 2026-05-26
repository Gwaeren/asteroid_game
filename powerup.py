import pygame
from circleshape import CircleShape
from constants import *

class RapidShot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWERUP_RADIUS)

    def draw(self, screen):
        half_size = POWERUP_SIDE_SIZE / 2
        rect = pygame.Rect(
            self.position.x - half_size,
            self.position.y - half_size,
            POWERUP_SIDE_SIZE,
            POWERUP_SIDE_SIZE,
        )
        pygame.draw.rect(screen, POWERUP_COLOR, rect)

        font = pygame.font.Font(None, SCORE_FONT_SIZE)
        text = font.render("R", True, POWERUP_TEXT_COLOR)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)
