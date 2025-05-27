import pygame
from constants import *

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
		       		return
		pygame.Surface.fill(screen, (0,0,0))
		pygame.display.flip()
		dt = clock.tick(60)/1000



	print("Starting Asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()

