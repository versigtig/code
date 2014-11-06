import pygame
import random
from controllers import *
from stuff import *
from lcolor import *

def setup():
	global MASTER
	MASTER = MasterController(SCREENSIZE,SCREENTITLE,FRAMERATE)
	
	#stars = Starfield()
	#MASTER.list_add(stars)
	#stars.MASTER = MASTER
	#stars.wrap = MASTER.SCREENSIZE
	
	for i in range(3):
		mass = random.randrange(75,200)
		pos = [ random.randrange(0,SCREENSIZE[0]), random.randrange(0,SCREENSIZE[1]) ]
		color = [ random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255) ]
		planet = Planet( mass, pos, color)
		MASTER.game.planets.append(planet)
		MASTER.list_add(planet,False)
		planet.MASTER = MASTER
	
	border = 8
	limits = ( border, border, SCREENSIZE[0] - border, SCREENSIZE[1] - border)
	guy = Player(limits)
	MASTER.list_add(guy)
	guy.MASTER = MASTER

SCREENSIZE = (1280,800)
SCREENTITLE = "Dumb shit goes here."
FRAMERATE = 60

setup()

#Loop
while MASTER.events.TERMINATE == 0:
	MASTER.main_loop()