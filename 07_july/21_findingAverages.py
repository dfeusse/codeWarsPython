'''
Make a program that takes a list of a random amount (but will always have atleast 
	1 number in) of numbers and returns the average, or mean, of the numbers. 
Also the program should return "Incorrect" if the value entered is a string.

(Use integer division to divide the numbers, (if you actually use the division method))

Ex: If input is [70, 70, 70, 70, 70] the program should return 70 (for obvious reasons)
'''
from __future__ import division

def average(n):
	return "Incorrect" if isinstance(n, str) else float(sum(n) / len(n))

print average([5,10])

'''
def average(x):
    try: return sum(x) / len(x)
    except: return "Incorrect"

def average(x):
    return "Incorrect" if type(x) is str else sum(x)/len(x)
'''