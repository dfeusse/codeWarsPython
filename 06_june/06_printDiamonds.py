'''
his kata is to practice simple string output. Jamie is a programmer, and girlfriend of James. 
She likes diamonds, and this time she expects String of diamond from James. As James doesn't 
know how to do it, he needs your help.

Task:

You need to print a shape on the screen using asterisk ("*") characters.

The shape that will be returned from print method resembles a diamond, where the number 
provided as input represents the number of * printed on the middle line. The line above 
and below will be centered and will have 2 less * than the middle line. This reduction 
by 2 * for each line continues until a line with a single * is printed at the top and 
bottom of the figure.

Return null if input is even number (as it is not possible to print diamond with even number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python, Python students must implement the diamond(n) 
method instead, and return None for invalid input.
'''

def diamond(n):
	if n%2 == 0:
		return None
	else:
		for i in range(1,n+2,2):
			print '*' * i
		for i in reversed(range(1,n,2)):
			print '*' * i

print diamond(0)
print diamond(1)
print diamond(2)
print diamond(9)
