# --- Gamepad Learning ---
# === Johnathan Fisher ===
# How does that there input work, son?

# Import
import pygame

# --- FUNCTIONS ---

def draw_snowman(screen, x, y):
	pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
	pygame.draw.ellipse(screen, RED, [23+x, 20+y, 50, 50])
	pygame.draw.ellipse(screen, GREEN, [0+x, 65+y, 100, 100])

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

pygame.mouse.set_visible(False)

# variables
x_speed = 0
y_speed = 0
x_coord = 10
y_coord= 10

# MAIN GAME LOOP

while not done:

	# EVENTS
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -3
			if event.key == pygame.K_RIGHT:
				x_speed = 3
			if event.key == pygame.K_UP:
				y_speed = -3
			if event.key == pygame.K_DOWN:
				y_speed = 3
	
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

	# GAME LOGIC
	
	x_coord += x_speed
	y_coord += y_speed

	if x_coord >= RESOLUTION[0]:
		x_coord = RESOLUTION[0] - 50
	if y_coord >= RESOLUTION[1]:
		y_coord = RESOLUTION[1] - 50
	if x_coord <= 0:
		x_coord = 0
	if y_coord <= 0:
		y_coord = 0

	# mouse position
	pos = pygame.mouse.get_pos()

	# WIPE SCREEN
	
	screen.fill(BLACK)
	
	# DRAWING

	draw_snowman(screen, x_coord, y_coord)
		
	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(FPS)

pygame.quit()