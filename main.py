# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_clock = pygame.time.Clock()
    delta_time_value = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "#000000")
        pygame.display.flip()
        tick_value = main_clock.tick(60)
        delta_time_value = tick_value / 1000

if __name__ == "__main__":
    main()