from controller import *
from gameobjects import *
import pygame
import sys

def setup(res,fps):
	pygame.init()
	MAIN = MainControl(res,fps)
	print("Master controller created.")
	return MAIN

def main_loop(MAIN):
	while MAIN.TERMINATE == 0:
		MAIN.EVENTS.check()
		if MAIN.TERMINATE != 0:
			print("Terminating.")
			pygame.quit()
			sys.exit()
		MAIN.update()
		MAIN.draw()
		MAIN.CLOCK.tick()

resolution = (1280,960)
fps = 60

ultra = setup(resolution,fps)
ultra.GAME.start()
main_loop(ultra)