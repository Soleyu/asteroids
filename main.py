# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
    
    #Variables
    updatables = pygame.sprite.Group()
    drawables  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatables, drawables)
    asteroid.Asteroid.containers = (asteroids, updatables, drawables)
    shot.Shot.containers = (shots, updatables, drawables)
    asteroidfield.AsteroidField.containers = (updatables)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    delta_time_value = 0
    running = True
    
    #objects
    main_clock = pygame.time.Clock()
    main_player = player.Player(x, y)
    main_field = asteroidfield.AsteroidField()
   
    #function calls
    pygame.init()
        
    #Main Loop
    while running:
        
        #deltatime
        tick_value = main_clock.tick(60)
        delta_time_value = tick_value / 1000
        
        #Inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #update
        for updatable in updatables:
            updatable.update(delta_time_value)
            
        #collision
        for aster in asteroids:
            if aster.is_collided(main_player):
                print("Game Over!")
                running = False
            for bullet in shots:
                if aster.is_collided(bullet):
                    aster.split()
                    bullet.kill()
        
        
        #draw
        pygame.Surface.fill(screen, "#000000")
        for drawable in drawables:
            drawable.draw(screen)
        
        #refresh
        pygame.display.flip()
        
    pygame.quit()



if __name__ == "__main__":
    main()