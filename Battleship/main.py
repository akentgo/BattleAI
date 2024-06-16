import pygame
import sys

pygame.init() #we need to initialize the instance
screen = pygame.display.set_mode((400, 300)) #We make a 400x300 window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Exits with a keypress
            pygame.quit()
            sys.exit()