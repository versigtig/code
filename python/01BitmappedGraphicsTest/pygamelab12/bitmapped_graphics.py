# --- Learn Pygame Lab 12--
# === Johnathan Fisher ===
# Loading sounds, sprites, and other graphics and using them.

# Import

import pygame

#Global Constants

FPS = 60
RESOLUTION = (640, 480)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize game engine

pygame.init()

# Open window

screen = pygame.display.set_mode(RESOLUTION)

#Load resources

background_image = pygame.image.load("AA_arne_palette.gif").convert()

ship_image = pygame.transform.scale2x(pygame.image.load("ship.png").convert())

#Other Opening Stuff 

pygame.display.set_caption("BitmappedGraphics")

done = False

clock = pygame.time.Clock()

ship_position = [0, 0]
x_speed = 0
y_speed = 0

circle_position = [50,50]

circle_size = 10
#FUNCTION JUNCTION WHAT IS YOUR MALFUNCTION

def draw_thing(screen, position, size):
	pygame.draw.circle(screen, RED, position, size)

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_speed = -3
			if event.key == pygame.K_DOWN:
				y_speed = 3
			if event.key == pygame.K_LEFT:
				x_speed = -3
			if event.key == pygame.K_RIGHT:
				x_speed = 3

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
	# GAME LOGIC

	ship_position[0] += x_speed
	ship_position[1] += y_speed

	circle_size = ((ship_position[0] + ship_position[1]) / 2) / 10
	if circle_size < 1:
		circle_size = 0

	circle_position = [ship_position[0] - 50 , ship_position[1] - 50]

	# WIPE SCREEN
	
	screen.fill(BLACK)
	
	# DRAWING
	
	screen.blit(background_image, [0, 0])
	screen.blit(ship_image, [ship_position[0] ,ship_position[1]])
	draw_thing(screen, circle_position, circle_size)

	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()