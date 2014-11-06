import pygame
import random
from lcolor import COLORS
import lfunc
import math

class ParticleEmitter():
	def __init__(self,pos=[0,0],angle=0,speed=1,life=120,num=1,color=COLORS.WHITE,repeat=0):
		self.pos = pos
		if isinstance(angle,list):
			self.angle_min = angle[0]
			self.angle_max = angle[1]
		else:
			self.angle_min,self.angle_max = angle,angle
		
		if isinstance(speed,list):
			self.speed_min = speed[0]
			self.speed_max = speed[1]
		else:
			self.speed_min,self.speed_max = speed,speed
		
		if isinstance(life,list):
			self.life_min = life[0]
			self.life_max = life[1]
		else:
			self.life_min,self.life_max = life,life
		
		if isinstance(num,list):
			self.num_min = num[0]
			self.num_max = num[1]
		else:
			self.num_min,self.num_max = num,num
		
		self.color = color
		self.timer = repeat
		self.time = repeat
		
		self.particles = []
		if self.num_min == self.num_max:
			number = self.num_min
		else:
			number = random.randrange(self.num_min,self.num_max)
		
		for i in range(number):
			self.particles.append([])
			self.particles[i].append(pos[0])
			self.particles[i].append(pos[1])
			self.particles[i].append(random.random() * (self.angle_max - self.angle_min) + self.angle_min)
			self.particles[i].append(random.random() * (self.speed_max - self.speed_min) + self.speed_min)
			if self.life_min == self.life_max:
				lifo = self.life_min
			else:
				lifo = random.randrange(self.life_min,self.life_max)
			self.particles[i].append(lifo)
			
			
	def update(self):
		i = 0
		while i < len(self.particles):
			self.particles[i][0] += lfunc.lengthdir_x(self.particles[i][3],self.particles[i][2])
			self.particles[i][1] += lfunc.lengthdir_y(self.particles[i][3],self.particles[i][2])
			self.particles[i][4] -= 1
			if self.particles[i][4] <= 0:
				del self.particles[i]
				i -= 1
			i += 1
		
		if len(self.particles) == 0 and self.timer == 0:
			self.MAIN.del_ref(self)
		'''
		for part in self.particles:
			part[0] += lfunc.lengthdir_x(part[3],part[2])
			part[1] += lfunc.lengthdir_y(part[3],part[2])
			part[4] -= 1
			if part[4] <= 0:
				del part
		'''
		
		if self.timer != 0:
			self.time -= 1
			if self.time <= 0:
				offset = len(self.particles)
				if self.num_min == self.num_max:
					number = self.num_min
				else:
					number = random.randrange(self.num_min,self.num_max)
				for i in range(number):
					self.particles.append([])
					self.particles[i + offset].append(self.pos[0])
					self.particles[i + offset].append(self.pos[1])
					self.particles[i + offset].append(random.random() * (self.angle_max - self.angle_min) + self.angle_min)
					self.particles[i + offset].append(random.random() * (self.speed_max - self.speed_min) + self.speed_min)
					if self.life_min == self.life_max:
						lifo = self.life_min
					else:
						lifo = random.randrange(self.life_min,self.life_max)
					self.particles[i + offset].append(lifo)
				self.time = self.timer
	
	def draw(self,surface):
		info = self.MAIN.FONT.render("Particles: " + str(len(self.particles)),True,COLORS.WHITE)
		surface.blit(info,[self.pos[0],self.pos[1] + 15])
		for part in self.particles:
			pygame.draw.line(surface,self.color,[part[0],part[1]],[part[0],part[1]])
			

class PartSplosions():
	wait = False
	def update(self):
		buttons = pygame.mouse.get_pressed()
		if buttons[0] and not self.wait:
			pos = pygame.mouse.get_pos()
			#part = ParticleEmitter(pos)
			#ParticleEmitter( [x,y], angle [min_angle,max_angle], speed, life, number, color, repeat timer)
			part = ParticleEmitter(pos,[80,100],[1,8],[80,100],[1,10],COLORS.RED,5)
			part.MAIN = self.MAIN
			self.MAIN.add_ref(part)
			self.wait = True
		elif buttons[0] == False:
			self.wait = False
	
	def draw(self,surface):
		info = self.MAIN.FONT.render("Partsplosion is hea",True,COLORS.WHITE)
		surface.blit(info,[5,5])
class Player(pygame.sprite.Sprite):
	#My movement code fucking sucks and I don't know why
	dir,thrust_x,thrust_y = [0]*3
	speed = [0,0]
	max_speed = 8
	thrust = 0.2
	friction = 0.05
	impulse = [False,False,False,False] #Thrust checkers
	thrust_dir = -1
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface([32,32])
		self.image.fill(COLORS.WHITE)
		self.image.set_colorkey(COLORS.WHITE)
		self.rect = self.image.get_rect()
		#self.pos = [self.rect.x + self.rect.width*.5,self.rect.y + self.rect.height*.5]
		self.pos = [self.rect.x,self.rect.y]
		
		#shape = []
		#pygame.draw.polygon(
		#by drawing into self.image I am modifying the sprite
		#This could be used for things like drawing transparent shapes onto sprites
		#to make destructable terrain (It's how worms did it)
		pygame.draw.circle(self.image,COLORS.PURPLE,[ self.rect.width//2, self.rect.height//2 ],min(self.rect.width,self.rect.height)//2)
		#pygame.draw.circle(self.image,COLORS.BLUE,[16,16],16)
	
	def update(self):
		#rep = len( self.MAIN.EVENTS.move )
		rep = 4
		for i in range(rep):
			if self.MAIN.EVENTS.move[i]: #Read events values
				self.impulse[i] = True
				#This if chain forces opposing thrust off
				#This mainly makes controls override eachother
				#So that right doesnt always triumph over left based on the order it was coded
				#And it possible should be handled by the event controller
				#To apply the same effect to menus or anything else
				#Done
				'''
				if i == 0:
					self.impulse[2] == False
				elif i == 1:
					self.impulse[3] == False
				elif i == 2:
					self.impulse[0] == False
				elif i == 3:
					self.impulse[1] == False
				'''
			else:
				self.impulse[i] = False
		
		#you can probably ignore this shit because it doesn't work anyways
		#And I will likely totally scrap it
		if self.impulse[0]: #RIGHT
			self.thrust_x = 1
		if self.impulse[2]: #LEFT
			self.thrust_x = -1
		if self.impulse[0] == 0 and self.impulse[2] == 0:
			self.thrust_x = 0
		if self.impulse[3]: #DOWN
			self.thrust_y = 1
		if self.impulse[1]: #UP
			self.thrust_y = -1
		if self.impulse[1] == 0 and self.impulse[3] == 0:
			self.thrust_y = 0
		if self.thrust_x == 0 and self.thrust_y == 0:
			self.thrust_dir = -10
		else:
			self.thrust_dir = lfunc.angle([self.thrust_x,self.thrust_y])
		'''
		#Check thrust and apply it or apply friction if there is no thrust
		if self.thrust_x != 0:
			self.speed[0] += lfunc.lengthdir_x(self.thrust,self.thrust_dir)
		#Friction is fucked so I'll disable it for now
		
		else:
			if abs(self.speed[0]) > self.friction:
				self.speed[0] -= math.copysign(1,self.speed[0])*self.friction
			else:
				self.speed[0] = 0
		
		if self.thrust_y != 0:
			self.speed[1] += lfunc.lengthdir_y(self.thrust,self.thrust_dir)
		
		else:
			if abs(self.speed[1]) > self.friction:
				self.speed[1] -= math.copysign(1,self.speed[1])*self.friction
			else:
				self.speed[1] = 0
		'''
		
		if self.thrust_dir != -10: #Only -1 if no thrust is applied
			if self.thrust_x != 0:
				self.speed[0] += lfunc.lengthdir_x(self.thrust,self.thrust_dir)
			if self.thrust_y != 0:
				self.speed[1] += lfunc.lengthdir_y(self.thrust,self.thrust_dir)
			self.dir = lfunc.angle(self.speed)
			#Constrain max speed for x and y to the proper lengthdir variants
			if abs(self.speed[0]) > abs(self.max_speed):
				self.speed[0] = math.copysign(self.max_speed,self.speed[0])
			if abs(self.speed[1]) > abs(self.max_speed):
				self.speed[1] = math.copysign(self.max_speed,self.speed[1])
			'''
			max_speed_x,max_speed_y = lfunc.lengthdir(self.max_speed,self.dir)
			if abs(self.speed[0]) > abs(max_speed_x):
				self.speed[0] = max_speed_x
			if abs(self.speed[1]) > abs(max_speed_y):
				self.speed[1] = max_speed_y
			'''
		else:
			if abs(self.speed[0]) > self.friction:
				self.speed[0] -= math.copysign(self.friction,self.speed[0])
			else:
				self.speed[0] = 0
			if abs(self.speed[1]) > self.friction:
				self.speed[1] -= math.copysign(self.friction,self.speed[1])
			else:
				self.speed[1] = 0
		
		
		#I was applying the speed twice! NO wonder it was so fucked!
		#self.rect.x += self.speed[0]
		#self.rect.y += self.speed[1]
		#Thrust right and left
		''' OLD CODE
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
		'''
		#Bounce off edges
		if self.rect.x < 0:
			self.speed[0] = abs(self.speed[0])
		if self.rect.x > self.MAIN.SCREENSIZE[0] - self.rect.width:
			self.speed[0] = abs(self.speed[0])*-1
		if self.rect.y < 0:
			self.speed[1] = abs(self.speed[1])
		if self.rect.y > self.MAIN.SCREENSIZE[1] - self.rect.height:
			self.speed[1] = abs(self.speed[1])*-1
		
		#And finally apply the actual speed to the object
		self.dir = lfunc.angle(self.speed)
		#self.rect.x += lfunc.lengthdir_x(abs(self.speed[0]),self.dir)
		#self.rect.y += lfunc.lengthdir_y(abs(self.speed[1]),self.dir)
		self.pos[0] += self.speed[0]
		self.pos[1] += self.speed[1]
		self.rect.x = int(self.pos[0])
		self.rect.y = int(self.pos[1])
		
		
		
	def draw(self,surface):
		poss = self.pos
		#Debug stuff
		posd = self.MAIN.FONT.render("Pos: [ " + str(poss[0]) + ", " + str(poss[1]) + " ]",True,COLORS.WHITE)
		speedd = self.MAIN.FONT.render("Speed: [ " + str(self.speed[0]) + ", " + str(self.speed[1]) + " ]",True,COLORS.WHITE)
		
		middle = [poss[0] + self.rect.width*.5,poss[1] + self.rect.height*.5]
		pygame.draw.line(surface,COLORS.LIME,middle,lfunc.lengthdir(100,self.dir,middle),1)
		if self.thrust_dir != -10:
			pygame.draw.line(surface,COLORS.RED,middle,lfunc.lengthdir(50,self.thrust_dir,middle),1)
		surface.blit(posd,[poss[0],poss[1] - 18])
		surface.blit(speedd,[poss[0],poss[1] - 36])

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