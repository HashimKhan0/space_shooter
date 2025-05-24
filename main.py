import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys 
from shooting import * 

def main():
	
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()



	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)


	Player.containers = (updatable, drawable)
	# initalizing a player
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT /2 
	player = Player(x,y)


	dt = 0 


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides(player):
				sys.exit("Game Over!")

			for shot in shots:
				if asteroid.collides(shot):
					#asteroid.kill()
					#shot.kill()
					asteroid.split()


		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
