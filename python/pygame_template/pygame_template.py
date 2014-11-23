'''
Pygame Template
versigtig
Template for the main file of a pygame project.
Requires variables.py for GLOBAL  variables.
'''

''' --- Setup --- '''
# Import
import pygame

# Pygame window setup and initialization
pygame.init()
screen = pygame.display.set_mode(GLOBALS.RESOLUTION)
pygame.display.set_caption("Star")
clock = pygame.time.Clock()

# Variables

''' --- Main Game Loop --- '''
while not done:

	# Events
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# Game logic
	
	# Wipe screen
	
	screen.fill(WHITE)
	
	# Drawing
	
	# Update screen
	
	pygame.display.flip()
	
	clock.tick(GLOBAL.FPS)

pygame.quit()