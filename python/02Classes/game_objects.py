import pygame
import random
from variables import GLOBALS
from my_color import COLORS

do_color = COLORS()



class Star():

	''' --- Attributes --- '''

	x = 0
	y = 0

	x_vector = 0
	y_vector = 0

	size = 10

	color = [255,255,255]

	x_tail = 1
	y_tail = 1

	''' --- Methods --- '''

	def __init__(self):
		self.x = random.randrange(0, GLOBALS.RESOLUTION[0])
		self.y = random.randrange(0, GLOBALS.RESOLUTION[1])
		self.x_vector = random.randrange(-8, 8)
		self.y_vector = random.randrange(-8, 8)
		self.size = random.randrange(1, 10)
		self.color = do_color.randgray(155,255)

	def move(self):
		self.x += self.x_vector
		self.y += self.y_vector
		if self.x > 660:
			self.x = -20
		elif self.x < -20:
			self.x = 660
		if self.y > 500:
			self.y = -20
		elif self.y < -20:
			self.y = 500


	def draw(self, screen):
		pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

	
	def draw_tail(self, screen):
		# THIS DOESN'T WORK I COULD SPEND MORE TIME ON IT BUT NAH
		'''
		if self.x_vector > 0:
			self.x_tail = -1 * x_vector
		else
			self.x_tail = 1 * x_vector
		if self.y_vector > 0:
			self.y_tail = -1
		else
			self.y_tail = 1
		'''

		pygame.draw.circle(screen, self.color, [self.x - self.x_vector, self.y - self.x_vector], int(self.size - self.size * 0.8))
		pygame.draw.circle(screen, self.color, [self.x - self.x_vector * 2, self.y - self.x_vector * 2], int(self.size -  self.size * 0.6))
		pygame.draw.circle(screen, self.color, [self.x - self.x_vector * 3, self.y - self.x_vector * 3], int(self.size -  self.size * 0.4))
		pygame.draw.circle(screen, self.color, [self.x - self.x_vector * 4, self.y - self.x_vector * 4], int(self.size -  self.size * 0.2))

