#!/usr/bin/python2

import cairo

#function from http://en.wikipedia.org/wiki/Primality_test
def is_prime(n):
        if n < 2:
                return False
        if n in (2, 3):
                return True
        if n % 2 == 0 or n % 3 == 0:
                return False
        max_divisor = int(n ** 0.5) # square root of n
        divisor = 5
        while divisor <= max_divisor:
                if n % divisor == 0 or n % (divisor + 2) == 0:
                        return False
                divisor += 6
        return True




def draw(WIDTH, HEIGHT):
 
	surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
	ctx = cairo.Context (surface)
	
	#set background color to black
 	ctx.set_source_rgb(0,0,0)
 	#create rectangle for background
 	ctx.rectangle (0, 0, WIDTH, HEIGHT)
 	#fill
 	ctx.fill()
 	ctx.set_source_rgb(0,1,1)
 
 	x = WIDTH/2
 	y = HEIGHT/2
 
 	pix_num = 1
 	arm_length = 1
 
 	while pix_num <= (WIDTH*HEIGHT):
  		i = 1
 		while i <= arm_length:
   			if (arm_length%4) == 1:
    				x += 1
   			elif (arm_length%4) == 2:
    				y +=1
   			elif (arm_length%4) == 3:
    				x -= 1 
   			else:
    				y -= 1
   			if is_prime(pix_num) == True:
    				ctx.rectangle(x,y,1,1)
           			ctx.fill()
   			i += 1
   			pix_num += 1
  		arm_length += 1
  
surface.write_to_png ("ulam.png")


draw(1000,1000)
