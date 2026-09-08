import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}. Screen width: {SCREEN_WIDTH}. Screen height: {SCREEN_HEIGHT}.")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0.0 
    while True:
        log_state()
        dt = Clock.tick(60) / 1000 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
if __name__ == "__main__":
    main()
