import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame_version = pygame.version.ver
    print(f"Starting Asteroids with pygame version: {pygame_version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
