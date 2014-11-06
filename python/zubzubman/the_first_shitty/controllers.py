import pygame
import sys
from lcolor import *

class DrawingController():
	draw_list = []
	sprite_list = []
	
	#Every visible object will send a reference into these lists.
	def __init__(self,screensize):
		self.surface = pygame.display.set_mode( screensize )
		self.surface.fill(COLORS.BLACK)
		self.fonto = pygame.font.SysFont( 'Courier New', 26, True, False )
		pygame.display.flip()
	
	def draw(self):
		self.surface.fill(COLORS.BLACK)
		#loop through the lists and execute teh draw method.
		for object in self.draw_list:
			object.draw(self.surface)
		for sprite in self.sprite_list:
			sprite.draw(self.surface)
		pygame.display.flip()


class GameController():
	update_list = []
	planets = []
	#every updating object will send a reference into this list
	def update(self):
		for object in self.update_list:
			object.update()


class EventController():
	TERMINATE = 0
	movekeys = [ 0, 0, 0 ,0 ] #left right up down
	power = 0
	rotate = 0
	fire = False
	
	def check(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.TERMINATE = 1
			#Key checks
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.movekeys[0] = 1
				if event.key == pygame.K_RIGHT:
					self.movekeys[1] = 1
				if event.key == pygame.K_UP:
					self.movekeys[2] = 1
				if event.key == pygame.K_DOWN:
					self.movekeys[3] = 1
				
				if event.key == pygame.K_w:
					self.power = 1
				if event.key == pygame.K_s:
					self.power = -1
				if event.key == pygame.K_q:
					self.rotate = 1
				elif event.key == pygame.K_e:
					self.rotate = -1
				if event.key == pygame.K_SPACE:
					self.fire = True
					
				if event.key == pygame.K_ESCAPE:
					self.TERMINATE = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					self.movekeys[0] = 0
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					self.movekeys[1] = 0
				if event.key == pygame.K_UP:
					self.movekeys[2] = 0
				if event.key == pygame.K_DOWN:
					self.movekeys[3] = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					self.power = 0
				if event.key == pygame.K_q or event.key == pygame.K_e:
					self.rotate = 0
				if event.key == pygame.K_SPACE:
					self.fire = False
			
	
class MasterController():
	
	def __init__(self,screensize,screentitle,framerate):
		pygame.init()
		self.SCREENSIZE = screensize
		self.FRAMERATE = framerate
		#Create controllers
		self.draw = DrawingController(screensize)
		self.events = EventController()
		self.game = GameController()
		self.clock = pygame.time.Clock()
	
	#Add to list method
	def list_add(self,object,u=True,d=True,s=False):
		if u:
			self.game.update_list.append(object)
		if d:
			self.draw.draw_list.append(object)
		if s:
			self.draw.sprite_list.append(object)
	
	def main_loop(self):
		self.events.check()
		if self.events.TERMINATE != 0:
			pygame.quit()
			sys.exit()
		self.game.update()
		self.draw.draw()
		self.clock.tick(self.FRAMERATE)