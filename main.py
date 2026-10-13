import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from logger import log_state
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}. Screen width: {SCREEN_WIDTH}. Screen height: {SCREEN_HEIGHT}.")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        log_state()
        dt = Clock.tick(60) / 1000
        for event in pygame.event.get():
            updatable.update(dt)
            for item in drawable:
                screen.fill("black")
                item.draw(screen)
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
if __name__ == "__main__":
    main()
