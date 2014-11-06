#Some functions
import pygame
import math

def check_mouse( x, y, x2, y2):
	"""Checks if the mouse is in the coordinates"""
	if pygame.mouse.get_pos[0] >= x and pygame.mouse.get_pos[0] <= x2:
		if pygame.mouse.get_pos[1] >= y and pygame.mouse.get_pos[1] <= y2:
			return True
		return False
	return False

def check_box( cx, cy, x1, y1, x2, y2 ):
	"""REturns true if [cx, cy] is in the rectangle [x1, y1, x2, y2]"""
	if cx >= x1 and cx <= x2:
		if cy >= y1 and cy <= y2:
			return True
		return False
	return False

def angle( target, origin=[0,0] ):
	"""Takes 2 [x,y] lists and returns angle compensating for relative positions"""
	#Raw distance
	x_raw = target[0] - origin[0]
	y_raw = target[1] - origin[1]

	#Absolute distance
	x = math.fabs( x_raw )
	y = math.fabs( y_raw )

	#SOH CAH TOA
	#Get the angle
	if x == 0:
		angle = 0.5 * math.pi
	elif y == 0:
		angle = 0
	else:
		angle = math.atan( y / x )

	# add to angle depending on relative position
	# 0 is right and it goes counter clockwise
	if x_raw <= 0:
		if y_raw <= 0:
			return math.degrees( math.pi - angle )
		else:
			return math.degrees( math.pi + angle )
	else:
		if y_raw <= 0:
			return math.degrees( angle )
		else:
			return math.degrees( 2 * math.pi - angle )
	
#My favorite functions that were built into game maker
def lengthdir_x( distance, direction ):
	"""Returns x vector by distance in direction"""
	x_distance = ( math.cos( direction ) * distance )
	return ( x_distance )
	
def lengthdir_y( distance, direction ):
	"""Returns y vector by distance in direction"""
	y_distance = ( math.sin( direction ) * distance ) * -1
	return ( y_distance )
	
#By your powers combined! Returns a list instead
def lengthdir( distance, direction, origin=[0,0] ):
	"""Returns origin[ x, y ] shifted by distance in direction"""
	dir = math.radians(direction)
	x_distance = origin[0] + ( math.cos( dir ) * distance )
	y_distance = origin[1] + ( math.sin( dir ) * distance ) * -1
	return [ x_distance, y_distance ]

def distance( origin, target ):
	
	"""Takes 2 [x,y] lists and returns the straight line (hypotenuse) distance"""
	distance_x = math.fabs( origin[0] - target[0] )
	distance_y = math.fabs( origin[1] - target[1] )

	return math.hypot( distance_x, distance_y )