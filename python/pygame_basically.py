# Import
import pygame

# Initialize game engine
pygame.init()

# Open window
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("The Quest")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

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
	
	offset = 0
	
	for x_offset in range(30,300,30):
		pygame.draw.line(screen,RED,[x_offset,100],[x_offset-10,90],2)
		pygame.draw.line(screen,RED,[x_offset,90],[x_offset-10,100],2)
	
	font = pygame.font.SysFont('Calibri',25,True,False)
	
	text = font.render("Anal Seepage",True,RED)
	
	screen.blit(text,[250,250])
	# UPDATE SCREEN
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()