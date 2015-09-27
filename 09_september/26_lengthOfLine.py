'''
Find the length between 2 co-ordinates. The co-ordinates are made of integers between -20 and 20 and will be given in the form of a 2D array:

(0,0) and (5,-7) would be [ [ 0 , 0 ] , [ 5, -7 ] ]

The function must return the answer rounded to 2 decimal places in the form of a string.

length_of_line([[0, 0], [5, -7]]) =&gt; "8.60"
If the 2 given co-ordinates are the same, the returned length should be "0.00"
'''
import math
def length_of_line(a):
	return "%.2f" % math.sqrt((a[0][0] - a[1][0])**2 + (a[0][1] - a[1][1])**2)


print length_of_line([[0, 0], [5, -7]])