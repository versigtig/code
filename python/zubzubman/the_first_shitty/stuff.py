import pygame
import random
from lcolor import COLORS
from lfunc import lengthdir,distance,calc_angle

class Planet():
	def __init__(self,size=100,position=[0,0],col=[255,255,255]):
		self.pos = [ position[0], position[1] ]
		self.mass = size*4
		self.color = col
		self.radius = self.mass // 8
	
	def draw(self,surface):
		pygame.draw.circle( surface, self.color, self.pos, self.radius )

class Projectile():
	radius = 6
	speed = [0,0]
	pos = [0,0]
	accel = [0,0]
	killzone = 1000
	
	def kill(self):
		self.MASTER.draw.draw_list.remove(self)
		self.MASTER.game.update_list.remove(self)
	
	def update(self):
		for planet in self.MASTER.game.planets:
			dist = distance( self.pos, planet.pos )
			if dist < planet.radius + self.radius//2:
				self.kill()
				return False
			if dist < planet.mass*8:
				self.accel = lengthdir( [0,0], 1/(dist*dist)*planet.mass, calc_angle(self.pos, planet.pos) )
				self.speed[0] += self.accel[0]
				self.speed[1] += self.accel[1]
		self.accel = [0,0]
		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]
		if self.pos[0] < -self.killzone or self.pos[0] > self.MASTER.SCREENSIZE[0] + self.killzone:
			if self.pos[1] < -self.killzone or self.pos[1] > self.MASTER.SCREENSIZE[1] + self.killzone:
				self.kill()
			'''
			try:
				self.MASTER.draw.draw_list.remove(self)
			except:
				print("no reference in draw list?")
			try:
				self.MASTER.game.update_list.remove(self)
			except:
				print("no reference in update list?")
			'''
			#self.cleanup()
			#need to find a way of safely destroying it and removing it from the master list
	
	def draw(self,surface):
		pygame.draw.circle( surface, COLORS.RED, [ int(self.pos[0]), int(self.pos[1])], self.radius )
	
class Player():
	radius = 48
	length = 48
	direction = 0
	pos = [ 200, 200 ]
	speed = 3
	rot_speed = 4
	btime = 0
	refire = 16
	power = 150
	minpower = 50
	maxpower = 500
	
	def __init__(self,area):
		self.limits = area
	
	def shoot(self):
		if self.btime > 0:
			return False
		bullet = Projectile()
		bullet.pos = lengthdir(self.mid,self.radius*2,self.direction)
		bullet.speed = lengthdir([0,0],self.power*0.01,self.direction)
		bullet.MASTER = self.MASTER
		self.MASTER.list_add(bullet)
		self.btime = self.refire
	
	def update(self):
		if self.MASTER.events.movekeys[0] == 1: #LEFT
			self.pos[0] -= self.speed
			if self.pos[0] <= self.limits[0]:
				self.pos[0] = self.limits[0]
		elif self.MASTER.events.movekeys[1] == 1: #RIGHT
			self.pos[0] += self.speed
			if self.pos[0] >= self.limits[2] - self.radius * 2:
				self.pos[0] = self.limits[2] - self.radius * 2
		if self.MASTER.events.movekeys[2] == 1: #UP
			self.pos[1] -= self.speed
			if self.pos[1] <= self.limits[1]:
				self.pos[1] = self.limits[1]
		elif self.MASTER.events.movekeys[3] == 1: #DOWN
			self.pos[1] += self.speed
			if self.pos[1] >= self.limits[3] - self.radius * 2:
				self.pos[1] = self.limits[3] - self.radius * 2
		if self.MASTER.events.power != 0:
			if self.MASTER.events.power == 1 and self.power < self.maxpower: #POWERU P
				self.power += 1
			if self.MASTER.events.power == -1 and self.power > self.minpower: #POWER DOWN
				self.power -= 1
		if self.MASTER.events.rotate == 1: #ROTATE LEFT
			self.direction += self.rot_speed
			if self.direction >= 360:
				self.direction -= 360
		elif self.MASTER.events.rotate == -1: #ROTATE RIGHT
			self.direction -= self.rot_speed
			if self.direction < 0:
				self.direction += 360
		if self.MASTER.events.fire:
			self.shoot()
		
		if self.btime > 0:
			self.btime -= 1
	
	def draw(self,surface):
		self.mid = [ self.pos[0] + self.radius * 0.5, self.pos[1] + self.radius * 0.5 ]
		pygame.draw.rect( surface, COLORS.PURPLE, [ self.pos[0], self.pos[1], self.radius, self.radius ] )
		pygame.draw.line( surface, COLORS.VIOLET, [ self.mid[0], self.mid[1] ], lengthdir(self.mid,self.radius*2,self.direction), 8)
		powah = self.MASTER.draw.fonto.render(str(self.power), True, COLORS.WHITE)
		surface.blit( powah, [ self.pos[0], self.pos[1] - 20 ] )
	
class Starfield():
	wrap = [1280,800]
	def __init__(self,number=75):
		self.x = []
		self.y = []
		self.rad = []
		for i in range(number):
			self.x.append( random.randrange(0, self.wrap[0]) )
			self.y.append( random.randrange(0, self.wrap[1]) )
			self.rad.append( random.randrange(1, 4) )
	
	def update(self):
		for i in range(len(self.x)):
			self.x[i] -= int(self.rad[i]*1.5)
			if self.x[i] <= 0:
				self.x[i] += self.wrap[0]
				self.y[i] = random.randrange(0, self.wrap[1])
	
	def draw(self,surface):
		for i in range(len(self.x)):
			pygame.draw.circle(surface,COLORS.randgray( 150, 150 + self.rad[i] * 17), [ self.x[i], self.y[i] ], self.rad[i])