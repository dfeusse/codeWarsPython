'''
Given two strings representing positive integers, such as "12" and "35", return a string containing 
their product.

Disabled

1. use of `eval`
2. use of ints
3. use of floats
4. use of unsigned longs
5. use of bitwise operators
Accepted

strings
booleans
arrays
Inputs will never have leading zeros, and neither should your output. Your function, multiplyMyNumbers, 
should handle numbers with up to 5 characters, "13255" for example.
'''
def multiply(a,b):
	return ' '.join([i for i in a.split() ])

print multiply('2','4')
print multiply('10','100')