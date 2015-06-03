'''
Complete the squareSum method so that it squares each number passed into it and then 
sums the results together.

For example:

square_sum([1, 2, 2]) # should return 9
'''

'''
def square_sum(array):
	sums = []
	for i in array:
		sums.append(i**2)
	return sum(sums)
'''

def square_sum(array):
	return sum([i**2 for i in array])

print square_sum([1,2,2])

'''
def square_sum(numbers):
    return sum(map(lambda x: x**2,numbers))

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)
'''