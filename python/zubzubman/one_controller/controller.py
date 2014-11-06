import random
import pygame
from gameobjects import *
from lcolor import COLORS

class EventControl():
	move = [False,False,False,False]
	
	def check(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.MAIN.TERMINATE = 1
			#Key checks
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.move[0] = True
				if event.key == pygame.K_UP:
					self.move[1] = True
				if event.key == pygame.K_LEFT:
					self.move[2] = True
				if event.key == pygame.K_DOWN:
					self.move[3] = True
				if event.key == pygame.K_ESCAPE:
					self.MAIN.TERMINATE = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.move[0] = False
				if event.key == pygame.K_UP:
					self.move[1] = False
				if event.key == pygame.K_LEFT:
					self.move[2] = False
				if event.key == pygame.K_DOWN:
					self.move[3] = False

class GameControl():
	update_list = []
	bullet_list = []
	RUNNING = False
	
	def __init__(self):
		""""""
	
	def update(self):
		print("Game update!")
		for obj in self.update_list:
			obj.update()
	
	def start(self,game=0):
		stars = Starfield()
		self.update_list.append(stars)
		self.MAIN.draw_list.append(stars)
		stars.MAIN = self.MAIN
		self.player = Player()
		self.player.rect.x = random.randrange(0,self.MAIN.SCREENSIZE[0])
		self.player.rect.y = random.randrange(0,self.MAIN.SCREENSIZE[1])
		self.update_list.append(self.player)
		self.MAIN.sprite_list.add(self.player)
		self.player.MAIN = self.MAIN
		self.RUNNING = True

class MainControl():
	draw_list = []
	sprite_list = pygame.sprite.Group()
	update_list = []
	TERMINATE = 0
	
	def __init__(self,screensize=(1280,960),framerate=60):
		self.SCREENSIZE = screensize
		self.MAXFPS = framerate
		self.SCREEN = pygame.display.set_mode( screensize )
		self.EVENTS = EventControl()
		self.EVENTS.MAIN = self
		self.GAME = GameControl()
		self.GAME.MAIN = self
		self.CLOCK = pygame.time.Clock()
	
	def add_ref(self,object,update=True,draw=True,sprite=False):
		if update:
			self.update_list.append(object)
		if draw:
			self.draw_list.append(object)
		if sprite:
			self.sprite_list.add(object)
	
	def update(self):
		#print("Main update!")
		for obj in self.update_list:
			obj.update()
		#print("Game running: ",self.GAME.RUNNING)
		if self.GAME.RUNNING:
			for obj in self.GAME.update_list:
				obj.update()
	
	def draw(self):
		self.SCREEN.fill(COLORS.BLACK)
		for obj in self.draw_list:
			obj.draw(self.SCREEN)
		self.sprite_list.draw(self.SCREEN)
		pygame.display.flip()