import pygame
import sys

# So I want to paint the Map itself, first I want to make a static array that is the Map itself

class Map:
		def __init__(self):
			self.map1 = [['a' for _ in range(5)] for _ in range(5)] #We have now made an array of 5x5 filled with 'a's
			self.map2 = [['a' for _ in range(5)] for _ in range(5)]

		def paint_Map(self, screen):
			line_color = (0,0,0) # first we store the color for the line and the width of said line
			line_width = 5
			center_x = screen.get_width() // 2 # If we resize the screen we need to adjust where the line would be this is why we use this variable
			# Using // 2 is a special division that removes the decimal number and rouns down to the nearest whole number
			pygame.draw.line(screen, line_color, (center_x, 0), (center_x, screen.get_height()), line_width)
			pygame.display.flip()
			
			tile_size = 119
			outline_width = 6
			screen_size = pygame.display.get_surface().get_size()
			width, height = screen_size
			x_offset = (width // 2) + ((outline_width-4) * 2)
			for y, row in enumerate(self.map1): #Creo la variable Y, para cada fila in 
				for x, element in enumerate(row):
					if element == 'a':
						pygame.draw.rect(screen, (255, 255, 255), (x*tile_size - outline_width/2, y*tile_size - outline_width/2, tile_size + outline_width, tile_size + outline_width))
						pygame.draw.rect(screen, (0,0,180), (x*tile_size, y*tile_size, tile_size, tile_size))
			for y, row in enumerate(self.map2): #Creo la variable Y, para cada fila in 
				for x, element in enumerate(row):
					if element == 'a':
						pygame.draw.rect(screen, (255, 255, 255), (x*tile_size + x_offset - outline_width/2, y*tile_size - outline_width/2, tile_size + outline_width, tile_size + outline_width))
						pygame.draw.rect(screen, (0,0,180), (x*tile_size + x_offset, y*tile_size, tile_size, tile_size))

						
