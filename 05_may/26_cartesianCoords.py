'''
Write a simple function that takes polar coordinates (an angle in degrees and a radius) 
and returns the equivalent cartesian coordinates (rouded to 10 places).

For example:

coordinates(90,1) = (0.0, 1.0)

coordinates(45, 1) = (0.7071067812, 0.7071067812)
'''
import math

def cartesian(angle,radius):
	x = math.cos(angle)*radius
	y = math.sin(angle)*radius
	print math.cos(angle)
	print math.sin(angle)
	return x,y

print cartesian(22.6,13)
