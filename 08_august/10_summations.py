'''
Make a program that will take an int (x) and give you the summation of 
all numbers from 1 up to x included. If the given input is not an integer, return "Error 404".

Examples:

summation(25)==325
summation(2.56)=="Error 404"
'''
def summation(n):
	#return sum(range(1,n+1))
	return sum(range(1,n+1)) if type(n) == int else "Error 404"

print summation(25)#==325
print summation(2.56)#=="Error 404"

'''
def summation(x):
    return sum(range(x+1)) if isinstance(x, int) else "Error 404";
'''