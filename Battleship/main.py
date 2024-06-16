import pygame
import sys

pygame.init() #we need to initialize the instance
screen = pygame.display.set_mode((1200, 600)) #We make a window
screen.fill((128,128,128)) #Fill the screen with gray


line_color = (0,0,0) # first we store the color for the line and the width of said line
line_width = 5
center_x = screen.get_width() // 2 # If we resize the screen we need to adjust where the line would be this is why we use this variable
# Using // 2 is a special division that removes the decimal number and rouns down to the nearest whole number
pygame.draw.line(screen, line_color, (center_x, 0), (center_x, screen.get_height()), line_width)
pygame.display.flip()
while True: # An infinite loop to keep the game running
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #It checks if current event is quit
			pygame.quit()
			sys.exit()