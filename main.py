# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player

def main():
    
    #Variables
    updatables = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    player.Player.containers = (updatables, drawables)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta_time_value = 0
    
    
    #objects
    main_clock = pygame.time.Clock()
    main_player = player.Player(x, y)
   
    #function calls
    pygame.init()
        
    #Main Loop
    while True:
        
        #deltatime
        tick_value = main_clock.tick(60)
        delta_time_value = tick_value / 1000
        
        #Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update
        for updatable in updatables:
            updatable.update(delta_time_value)
        
        #draw
        pygame.Surface.fill(screen, "#000000")
        for drawable in drawables:
            drawable.draw(screen)
        
        #refresh
        pygame.display.flip()



if __name__ == "__main__":
    main()