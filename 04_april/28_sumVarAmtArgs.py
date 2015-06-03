'''
Write a function sum that accepts an unlimited number of integer arguments,
 and adds all of them together.

The function should reject any arguments that are not integers, and sum 
the remaining integers.

sum(1,2,3) # =&gt; 6
'''

def sum(*args):
	theSum = 0
	for arg in args:
		if isinstance(arg, int) == True:
			theSum = theSum	+ arg
	return theSum


print sum(1,2,3,4)
print '--------'
print sum(5, "dan", 7, 8.5, 9)


'''
from __builtin__ import sum as builtin_sum
def sum(*args):
    return builtin_sum(arg for arg in args if isinstance(arg, int))

def sum(*args):
    return reduce(lambda p, n: p + (type(n) == int and n or 0), args, 0)
'''