import pygame
import random
from lcolor import COLORS
import lfunc
import math

class Player(pygame.sprite.Sprite):
	dir = 0
	speed = [0,0]
	max_speed = 4
	thrust = 0.05
	friction = 0.005
	impulse = [False,False,False,False]
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface([32,32])
		self.image.fill(COLORS.WHITE)
		self.image.set_colorkey(COLORS.WHITE)
		self.rect = self.image.get_rect()
		#self.pos = [self.rect.x + self.rect.width*.5,self.rect.y + self.rect.height*.5]
		
		#shape = []
		#pygame.draw.polygon(
		pygame.draw.circle(self.image,COLORS.PURPLE,[ self.rect.width//2, self.rect.height//2 ],min(self.rect.width,self.rect.height)//2)
		#pygame.draw.circle(self.image,COLORS.BLUE,[16,16],16)
	
	def update(self):
		#rep = len( self.MAIN.EVENTS.move )
		rep = 4
		for i in range(rep):
			if self.MAIN.EVENTS.move[i]: #Read events values
				self.impulse[i] = True
				if i == 0: #This if chain forces opposing thrust off
					self.impulse[2] == False
				elif i == 1:
					self.impulse[3] == False
				elif i == 2:
					self.impulse[0] == False
				elif i == 3:
					self.impulse[1] == False
			else:
				self.impulse[i] = False
		
		#Thrust right and left
		if self.impulse[0]:
			self.speed[0] += self.thrust
			if self.speed[0] > self.max_speed:
				self.speed[0] = self.max_speed
		elif self.impulse[2]:
			self.speed[0] -= self.thrust
			if self.speed[0] < -self.max_speed:
				self.speed[0] = -self.max_speed
		#Friction
		else:
			self.speed[0] -= math.copysign(self.friction,self.speed[0])
			if abs(self.speed[0]) <= self.friction:
				self.speed[0] = 0
		#Thrust up and down
		if self.impulse[3]:
			self.speed[1] += self.thrust
			if self.speed[1] > self.max_speed:
				self.speed[1] = self.max_speed
		elif self.impulse[1]:
			self.speed[1] -= self.thrust
			if self.speed[1] < -self.max_speed:
				self.speed[1] = -self.max_speed
		else:
			self.speed[1] -= math.copysign(self.friction,self.speed[1])
			if abs(self.speed[1]) <= self.friction:
				self.speed[1] = 0
		
		self.dir = lfunc.angle(self.speed)
		#self.rect.x += lfunc.lengthdir_x(abs(self.speed[0]),self.dir)
		#self.rect.y += lfunc.lengthdir_y(abs(self.speed[1]),self.dir)
		self.rect.x += self.speed[0]
		self.rect.y += self.speed[1]
		
		#Bounce off walls
		if self.rect.x < 0:
			self.speed[0] = abs(self.speed[0])
		elif self.rect.x > self.MAIN.SCREENSIZE[0] - self.rect.width:
			self.speed[0] = abs(self.speed[0])*-1
		if self.rect.y < 0:
			self.speed[1] = abs(self.speed[1])
		elif self.rect.y > self.MAIN.SCREENSIZE[1] - self.rect.height:
			self.speed[1] = abs(self.speed[1])*-1
		
		
class Starfield():
	x = []
	y = []
	speed = []
	bright = []
	
	def __init__(self,number=40,limits=[1280,960]):
		print("stars created")
		for i in range(number):
			self.x.append(random.randrange(0,limits[0]))
			self.y.append(random.randrange(0,limits[1]))
			self.speed.append(random.random()*2)
			self.bright.append(random.randrange(110,255))
	
	def update(self):
		for i in range(len( self.x )):
			self.x[i] -= self.speed[i]
			if self.x[i] < 0:
				self.x[i] = self.MAIN.SCREENSIZE[0] + 1
				self.y[i] = random.randrange(0,self.MAIN.SCREENSIZE[1])
	
	def draw(self,surface):
		for i in range(len( self.x )):
			pygame.draw.circle(surface,[self.bright[i],self.bright[i],self.bright[i]],[int(self.x[i]),int(self.y[i])],1)