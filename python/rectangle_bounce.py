# IMPORT

import pygame

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

pygame.display.set_caption("Rectangles")

clock = pygame.time.Clock()
done = False
rect_x = 50
rect_y = 50

rect_x_vector = 5
rect_y_vector = 5

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# GAME LOGIC
	
	if rect_x > 590:
		rect_x_vector = -5
	elif rect_x < 1:
		rect_x_vector = 5
	if rect_y > 430:
		rect_y_vector = -5
	elif rect_y < 1:
		rect_y_vector = 5
	
	rect_x += rect_x_vector
	rect_y += rect_y_vector
	
	# WIPE SCREEN
	
	screen.fill(BLACK)
	
	# DRAWING
	for i in range(10):
		pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
		pygame.draw.rect(screen, RED, [rect_x + i * 10,rect_y + i * 10,40,40])
		pygame.draw.rect(screen, BLUE, [rect_x + i * 2,rect_y + i * 2,30,30])
	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()