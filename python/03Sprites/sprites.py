'''
Sprite Test
versigtig
Testing out how sprites work.
'''

''' --- Setup --- '''
# Import
import pygame
import random
from game_objects import Block
from my_color import COLORS
from variables import GLOBALS

# Pygame window setup and initialization
pygame.init()
screen = pygame.display.set_mode(GLOBALS.RESOLUTION)
pygame.display.set_caption("Sprites")
clock = pygame.time.Clock()

## Variables ##

#This is a list of each block the player can collide with.
#The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

#This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

#Create enemy blocks.
for i in range(50):
	#This represents an enemy block.
	block = Block(COLORS.BLUE, 20, 20)

	#Set a random location for the block
	block.rect.x = random.randrange(GLOBALS.RESOLUTION[0])
	block.rect.y = random.randrange(GLOBALS.RESOLUTION[1])

	#Add the block to the list of objects
	block_list.add(block)
	all_sprites_list.add(block)

#Player block.
player = Block(COLORS.RED, 30, 30)
all_sprites_list.add(player)

#Loop until close button.
done = False

#Score
score = 0

#Can't see that mouse pointer
pygame.mouse.set_visible(False)

''' --- Main Game Loop --- '''
while not done:

	## Events ##
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	## Game logic ##

	# Get mouse position
	pos = pygame.mouse.get_pos()
	
	#Get the x and y out of the list then set them to the mouse position.
	player.rect.x = pos[0] 
	player.rect.y = pos[1]

	#Player block collided with anything?
	blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

	for block in blocks_hit_list:
		score += 1
		print(score)
	
	#Move all the enemy blocks
	block_list.update()
	
	## Drawing ##
	
	# Wipe screen
	screen.fill(COLORS.WHITE)
	
	# Draw all the sprites

	all_sprites_list.draw(screen)

	# Update screen
	
	pygame.display.flip()
	
	clock.tick(GLOBALS.FPS)

pygame.quit()