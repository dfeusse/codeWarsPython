'''
Complete the function circleArea so that it will return the area of a circle 
with the given radius. Round the returned number to two decimal places (except for Haskell). 
If the radius is not positive or not a number, return false.

Example:

circleArea(-1485.86)     #returns false
circleArea(0)            #returns false
circleArea(43.2673)      #returns 5881.25
circleArea(68)           #returns 14526.72
circleArea("number")     #returns false
'''

import math

def circleArea(r):
	if r <= 0 or type(r) == str:
		return False
	else:
		return round(math.pi * (r ** 2),2)

print circleArea(-1485.86)    #returns false
print circleArea(0)           #returns false
print circleArea(43.2673)     #returns 5881.25
print circleArea(68)          #returns 14526.72
print circleArea("number") 	# returns false

'''
def circleArea(r):
    return round(pi * r ** 2, 2) if type(r) in (int, float) and r > 0 else False

def circleArea(r):
    if r <= 0 or str(r).isdigit() == False:
        return False
    import math
    return round(math.pi*r**2, 2)

'''