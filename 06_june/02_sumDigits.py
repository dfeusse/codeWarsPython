'''
Write a function named sumDigits which takes a number as input and 
returns the sum of the absolute value of each of the number's decimal digits. 
For example:

sumDigits(10)  # Returns 1
sumDigits(99)  # Returns 18
sumDigits(-32) # Returns 5
'''

'''
def sumDigits(num):
	newsum = 0
	for i in str(abs(num)):
		newsum = newsum + int(i)
	return newsum
'''

def sumDigits(num):
	#return sum([ int(i) for i in str(abs(num)) ])
	return sum( int(i) for i in str(abs(num)) )

print sumDigits(10)  # Returns 1
print sumDigits(99)  # Returns 18
print sumDigits(-32) # Returns 5

'''
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))

def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number

 def sumDigits(number):
    return sum([int(i) for i in str(abs(number))])
'''
'''