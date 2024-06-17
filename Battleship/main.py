import pygame
import sys
from map import Map

pygame.init() #we need to initialize the instance
screen = pygame.display.set_mode((1200, 598)) #We make a window
screen.fill((128,128,128)) #Fill the screen with gray

map_instance = Map()
clock = pygame.time.Clock()

'''print(map_instance) THE MAP IS STORED OK
for row in map_instance.map:
	print(' '.join(row))'''
map_instance.paint_Map(screen)
pygame.display.flip()
while True: # An infinite loop to keep the game running
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #It checks if current event is quit
			pygame.quit()
			sys.exit()
	clock.tick(60)
if __name__ == "__main__":
	main()