import pygame
import random
from variables import GLOBALS
from my_color import COLORS

class Block(pygame.sprite.Sprite):
	'''
	This class represents the player.
	Derives from the "Sprite" class in pygame.
	'''

	''' --- Setup --- '''

	## Variables ##

	#Controls the wiggle in the y vector	
	y_counter = 0
	y_change = 1
	y_wiggle = 1

	def __init__(self, color, width, height):
		''' 
		Constructor. Pass in the color of the block,
		it's width and height.
		'''

		# Call the constructor of the Sprite class as well
		super(Block, self).__init__()

		# Create a new surface, fill it with white, then make it transparent.
		self.image = pygame.Surface([width, height])
		self.image.fill(COLORS.WHITE)
		self.image.set_colorkey(COLORS.WHITE)

		# Draw an ellipse the same width and height on the surface
		pygame.draw.ellipse(self.image, color, [0, 0, width, height])

		#Feth the rectangle object that has the dimensions of the image.
		#Can update the position of this object by setting values of rect.x and rect.y
		self.rect =self.image.get_rect()

	def update(self):
		'''
		Called each frame, moves the block
		in the pattern described.
		'''

		# THERE HAS GOT A BETTER WAY TO DO A Y-AXIS "WIGGLE" MOTION
		self.y_counter += self.y_change

		if self.y_counter > 20 or self.y_counter < -20:
			self.y_change = self.y_change * -1
			self.y_wiggle = self.y_wiggle * -1

		self.rect.y += self.y_wiggle
		self.rect.x += 2

		if self.rect.x > GLOBALS.RESOLUTION[0]:
			self.rect.x = 0
			self.rect.y = random.randrange(0, GLOBALS.RESOLUTION[1])
