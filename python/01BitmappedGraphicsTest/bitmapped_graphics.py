# --- Bitmapped Graphics and Sound--
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

ship_image = pygame.image.load("ship.png").convert()

ship_image = pygame.transform.scale2x(ship_image)
#Load resources

background_image = pygame.image.load("AA_arne_palette.gif").convert()

#Other Opening Stuff 

pygame.display.set_caption("BitmappedGraphics")

done = False

clock = pygame.time.Clock()

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# GAME LOGIC
	
	ship_position = pygame.mouse.get_pos()

	# WIPE SCREEN
	
	screen.fill(BLACK)
	
	# DRAWING
	
	screen.blit(ship_image, [ship_position[0] ,ship_position[1] ])

	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()