'''
Sum all array arguments.

Calculate the sum of all the given arguments.

Note: if any of the arguments values is not a number (a string, null/None/nil or other values), 
the function should return false/False instead of the sum of the arguments.
'''
def sumAll(*arg):
	sum = 0
	for i in arg:
		if isinstance(i, int) == False:
			return False
		else:
			sum = sum + i
	return sum
	
	#return sum( [ i for i in arg if isinstance(i,int)==True ] )

print sumAll(1,2,3)
print sumAll(100,100,50)
print sumAll(1, None, 2)
print sumAll(1, "dan")

'''
def sum_all(*a):
    try:
        return sum(a)
    except:
        return False
        '''