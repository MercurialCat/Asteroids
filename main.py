import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from weapons import Shot


def main():
    print("Starting asteroids!") #starting parameters
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #REMEMBER TO ACTUALLY INIT YOUR MODULES HAHAH
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #screen size
    fps = pygame.time.Clock() #setting fps/clock

    asteroidfield = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #player size on screen
    asteroid_field = AsteroidField()
    dt = 0 #delta time



    while True:  #This is the start of the game loop, *where all the *magic* happens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        
        for object in asteroids:
            if object.collision(player):
                print("Game over!") 
                sys.exit()

        screen.fill(("black"))

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = fps.tick(60) / 1000 # framerate set to 60
       




      

if __name__ == "__main__":
    main()