import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_clock = pygame.time.Clock()
    font = pygame.font.Font(None, SCORE_FONT_SIZE)
    dt = 0
    score = 0
    lives = PLAYER_LIVES

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = frame_clock.tick(60) / 1000
        updatable.update(dt)
        screen.fill(SCREEN_COLOR)

        for item in drawable:
            item.draw(screen)

        pygame.draw.rect(screen, SCORE_BAR_COLOR, (0, 0, SCREEN_WIDTH, SCORE_BAR_HEIGHT))
        score_text = font.render(f"Score: {score}", True, SCORE_TEXT_COLOR)
        screen.blit(score_text, (30, 10))
        lives_text = font.render(f"Lives: {lives}", True, SCORE_TEXT_COLOR)
        screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 30, 10))

        for item in asteroids:
            if item.collides_with(player) and not player.is_invincible():
                log_event("player_hit")
                lives -= 1

                if lives <= 0:
                    print(f"Game over! Your score is {score}")
                    sys.exit()

                player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        for asteroid in asteroids:
            for one_shot in shots:
                if asteroid.collides_with(one_shot):
                    log_event("asteroid_shot")
                    score += 1
                    asteroid.split()
                    one_shot.kill()

        pygame.display.flip()


if __name__ == "__main__":
    main()
