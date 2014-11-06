import random

class COLORS():
	BLACK = ( 0, 0, 0 )
	DARKGRAY = ( 63, 63, 63 )
	GRAY = ( 127, 127, 127 )
	LIGHTGRAY = ( 191, 191, 191 )
	DARKGREY = ( 63, 63, 63 )
	GREY = ( 127, 127, 127 )
	LIGHTGREY = ( 191, 191, 191 )
	WHITE = ( 255, 255, 255 )
	RED = ( 255, 0, 0 )
	ORANGE = ( 255, 127, 0 )
	YELLOW = ( 255, 255, 0 )
	LIME = ( 70, 255, 70 )
	GREEN = ( 0, 177, 0 )
	TEAL = ( 50, 255, 255 )
	TURQUOISE = ( 0, 177, 255 )
	BLUE = ( 0, 0, 255 )
	DEEPBLUE = ( 0, 0, 140 )
	PURPLE = ( 100, 0, 255 )
	VIOLET = ( 220, 0, 255 )
	PINK = ( 255, 0, 200 )
	
	'''
	rand_gray = random.randrange( 0, 255 )
	last_random = [ random.randrange( 0, 255 ), random.randrange( 0, 255 ), random.randrange( 0, 255 ) ]
	last_gray = [ rand_gray, rand_gray, rand_gray ]
	last_combo = [ 0, 0, 0 ]
	'''
	
	def random(self):
		#self.last_random = [ random.randrange( 0, 255 ), random.randrange( 0, 255 ), random.randrange( 0, 255 ) ]
		#return self.last_random
		return [ random.randrange( 0, 255 ), random.randrange( 0, 255 ), random.randrange( 0, 255 ) ]

	def randgray(self,min=0,max=255):
		#self.rand_gray = random.randrange( 0, 255 )
		#self.last_gray = [ rand_gray, rand_gray, rand_gray ]
		#return self.last_gray
		r = random.randrange( min, max )
		return ( r, r, r )

	def combine( self, color1, color2 ):
		#last_combo = [ ( color1[0] + color2[0] ) // 2, ( color1[1] + color2[1] ) // 2, ( color1[2] + color2[2] ) // 2 ]
		#return last_combo
		return [ min( 255, (color1[0] + color2[0]) // 2 ), min( 255, (color1[1] + color2[1]) // 2 ), min( 255, (color1[2] + color2[2]) // 2 ) ]

	def alter( self, color, r, g, b ):
		#last_alter = [ color[0] + r, color[1] + g, color[2] + b ]
		#return last_alter
		return [ max( 0, min( 255, color[0] + r ) ), max( 0, min( 255, color[1] + g ) ), max( 0, min( 255, color[2] + b ) ) ]