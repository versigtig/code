import random
import pygame
from gameobjects import *
from lcolor import COLORS

class EventControl():
	move = [False,False,False,False] #RIGHT UP LEFT DOWN respectively
	
	def check(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.MAIN.TERMINATE = 1
			#Key checks
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					self.move[0] = True
					self.move[2] = False
				if event.key == pygame.K_UP:
					self.move[1] = True
					self.move[3] = False
				if event.key == pygame.K_LEFT:
					self.move[2] = True
					self.move[0] = False
				if event.key == pygame.K_DOWN:
					self.move[3] = True
					self.move[1] = False
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
	bullet_list = [] #I don't even have bullets left
	RUNNING = False #Game only updates game objects if running is true
	
	def __init__(self):
		"""Do Nothing for now"""
	
	def update(self):
		#print("Game update!") #add a debug class that prints shit like this
		for obj in self.update_list:
			obj.update()
	
	def start(self,game=0):
		stars = Starfield()
		self.update_list.append(stars) #Add reference to GAME
		self.MAIN.draw_list.append(stars) #add reference to MAIN's drawlist
		stars.MAIN = self.MAIN #add a reference to the main controller EVERYTHING will be accessable thru it
		#self.player = Player()
		#self.player.rect.x = random.randrange(0,self.MAIN.SCREENSIZE[0])
		#self.player.rect.y = random.randrange(0,self.MAIN.SCREENSIZE[1])
		#self.update_list.append(self.player)
		#self.MAIN.sprite_list.add(self.player)
		#self.MAIN.add_ref(self.player,False,True,True)
		#self.player.MAIN = self.MAIN
		self.PARTS = PartSplosions()
		self.PARTS.MAIN = self.MAIN
		self.MAIN.add_ref(self.PARTS,True,False)
		self.RUNNING = True #START THIS SHIT SHOULD MAYBE

class MainControl():
	draw_list = [] #The main draw list ONLY REFERENCES TO THINGS WITH CUSTOM draw() goes in here.
	sprite_list = pygame.sprite.Group() #everything else will be sprites
	update_list = [] #Main update list this runs seerate from the game update future proofing for a pause and/or menu
	TERMINATE = 0 #0 = run. Anything that's not 0 = STOP
	
	def __init__(self,screensize=(1280,960),framerate=60):
		self.SCREENSIZE = screensize
		self.MAXFPS = framerate
		self.SCREEN = pygame.display.set_mode( screensize ) #Main drawing surface
		self.EVENTS = EventControl()
		self.EVENTS.MAIN = self #add reference to main (self)
		self.GAME = GameControl()
		self.GAME.MAIN = self #add reference to main 
		self.CLOCK = pygame.time.Clock() #Clock is needed for timing otherwise game runs as fast as it can
		self.FONT = pygame.font.SysFont( 'Courier New', 20, True, False ) #This will prolly be removed and put into a debug class
	
	def add_ref(self,object,update=True,draw=True,sprite=False):
		#ez add reference to list func. add_ref(object,add to update list?, draw list?, sprite list?)
		if update:
			self.update_list.append(object)
		if draw:
			self.draw_list.append(object)
		if sprite:
			self.sprite_list.add(object)
	
	def del_ref(self,object,update=True,draw=True,sprite=False):
		#ez add reference to list func. add_ref(object,add to update list?, draw list?, sprite list?)
		if update:
			self.update_list.remove(object)
		if draw:
			self.draw_list.remove(object)
		if sprite:
			self.sprite_list.remove(object)
	
	def update(self):
		#print("Main update!")
		#call update() on everything in the main update list
		for obj in self.update_list:
			obj.update()
		#print("Game running: ",self.GAME.RUNNING)
		if self.GAME.RUNNING:
			#If the game is running call update() on everything in GAME.update_list
			for obj in self.GAME.update_list:
				obj.update()
	
	def draw(self):
		self.SCREEN.fill(COLORS.BLACK) #Blank the screen
		#Call draw() on anything in drawlist
		for obj in self.draw_list:
			obj.draw(self.SCREEN)
		#only one command needed to draw every sprite in the group! nice!
		self.sprite_list.draw(self.SCREEN)
		pygame.display.flip() #Update the screen