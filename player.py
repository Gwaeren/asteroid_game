import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.invincibility_timer = 0
        self.rapid_shot_timer = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = "white"
        if self.is_invincible():
            color = "yellow"
        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= dt
        self.invincibility_timer -= dt
        self.rapid_shot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.wrap_around()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.shot_cooldown_timer > 0:
            return
        if self.rapid_shot_timer > 0:
            cooldown_timer /= 2
        self.shot_cooldown_timer = cooldown_timer
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def is_invincible(self):
        return self.invincibility_timer > 0

    def respawn(self, x, y):
        self.position.x = x
        self.position.y = y
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.invincibility_timer = PLAYER_RESPAWN_INVINCIBILITY_SECONDS

    def activate_rapid_shot(self):
        self.rapid_shot_timer = PLAYER_RAPID_SHOT_DURATION_SECONDS

    def has_rapid_shot(self):
        return self.rapid_shot_timer > 0
