import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#   pygame_version = pygame.version.ver
#   print(f"Starting Asteroids with pygame version: {pygame_version}")
#   print(f"Screen width: {SCREEN_WIDTH}")
#   print(f"Screen height: {SCREEN_HEIGHT}")
    frame_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = frame_clock.tick(60) / 1000
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
