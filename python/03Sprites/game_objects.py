import pygame
from my_color import COLORS

class Block(pygame.sprite.Sprite):
	'''
	This class represents the player.
	Derives from the "Sprite" class in pygame.
	'''

	def __init__(self, color, width, height):
		''' 
		Constructor. Pass in the color of the block,
		it's width and height.
		'''

		# Call the constructor of the Sprite class as well
		super().__init__()

		# Create a new surface, fill it with white, then make it transparent.
		self.image = pygame.Surface([width, height])
		self.image.fill(COLORS.WHITE)
		self.image.set_colorkey(COLORS.WHITE)

		# Draw an ellipse the same width and height on the surface
		pygame.draw.ellipse(self.image, color, [0, 0, width, height])

		#Feth the rectangle object that has the dimensions of the image.
		#Can update the position of this object by setting values of rect.x and rect.y
		self.rect =self.image.get_rect()