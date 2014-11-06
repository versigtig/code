'''
Class Tests
versigtig
Just testing out classes and objects.
'''

''' --- Setup --- '''
# Import
import pygame
import random
from game_objects import Star
from variables import GLOBALS
from my_color import COLORS

# Pygame window setup and initialization
pygame.init()
screen = pygame.display.set_mode(GLOBALS.RESOLUTION)
pygame.display.set_caption("Star")
clock = pygame.time.Clock()

# Variables
done = False

my_star = []
star_size = 2

for i in range(50):
	my_star.append(Star())

''' --- Main Game Loop --- '''
while not done:

	# Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# Game Logic
	
	# Wipe Screen
	
	screen.fill(COLORS.BLACK)
	
	# Drawing
	
	for i in range(len(my_star)):
		my_star[i].move()
		my_star[i].draw(screen)
		my_star[i].draw_tail(screen)

	# Update Screening
	
	pygame.display.flip()
	
	clock.tick(GLOBALS.FPS)

pygame.quit()