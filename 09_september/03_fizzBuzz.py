'''
FizzBuzz is probably the second most popular way to introduce beginners to the art of coding 
(the first probably being the ancient Fibonacci sequence, the grandfather of all the algorithm theory).

In this very basic kata you will have to create a function that returns the same numbers 
that is given as a parameter, with the following exceptions:

If number divides evenly with 3 - returns string "fizz"
If number divides evenly with 5 - returns string "buzz"
If number divides evenly with 3 and 5 - returns string "fizz buzz"
Sample cases:

fizzbuzz(1)==1
fizzbuzz(9)=="fizz"
fizzbuzz(25)=="buzz"
fizzbuzz(37)==37
fizzbuzz(45)=="fizz buzz"
'''
def fizzbuzz(n):
	if n % 3 == 0 and n % 5 == 0:
		print "fizz buzz"
    else:
		return "fizz"
	'''
	elif n % 5 == 0:
		return "buzz"
	else:
		return n
	'''

print fizzbuzz(1)==1
print fizzbuzz(9)=="fizz"
print fizzbuzz(25)=="buzz"
print fizzbuzz(37)==37
print fizzbuzz(45)=="fizz buzz"