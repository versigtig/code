# --- Chapter 11 Practice ---
# === Johnathan Fisher ===
# Practice for chapter 11 of Program Arcade Games.

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

pygame.display.set_caption("Template")

done = False

clock = pygame.time.Clock()

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# GAME LOGIC
	
	# WIPE SCREEN
	
	screen.fill(WHITE)
	
	# DRAWING
	
	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()