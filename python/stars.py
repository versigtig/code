# IMPORT

import pygame
import random

# INITIALIZE

pygame.init()

# CONSTANTS

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 60

RESOLUTION = (640, 480)

# SETUP

screen = pygame.display.set_mode(RESOLUTION)

pygame.display.set_caption("Stars")

clock = pygame.time.Clock()
done = False

star_list = []
star_size = 2

for i in range(50):
	x = random.randrange(0, RESOLUTION[0])
	y = random.randrange(0, RESOLUTION[1])
	star_list.append([x,y])

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# GAME LOGIC
	
	
	# WIPE SCREEN
	
	screen.fill(BLACK)
	
	# DRAWING
	
	for i in range(len(star_list)):
		star_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
		p ygame.draw.circle(screen, star_color, star_list[i], star_size)
		
		star_list[i][0] += random.randrange(0, 10)
		
		if star_list[i][0] > RESOLUTION[0]:
			star_list[i][0] = -1
			star_list[i][1] = random.randrange(0,RESOLUTION[1])
			star_size = random.randrange(0,50)
		
	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()