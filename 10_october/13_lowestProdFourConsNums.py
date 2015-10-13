'''
Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.

This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example

lowest_product("123456789")--&gt; 24 (1x2x3x4)
lowest_product("35") --&gt; "Number is too small"
'''
import sys

def lowest_product(string):
	if len(string) <= 4:
		return "Number is too small"
	else:
		product = sys.maxint
		index = 0
		newList = [ int(s) for s in string ]
		for a in newList[:len(string)-4]:
			tempProduct = a * newList[index+1] * newList[index+2] * newList[index+3]
			index+=1
			if tempProduct < product:
				product = tempProduct
	return product

print lowest_product("123456789")#--&gt; 24 (1x2x3x4)
print lowest_product("35") #--&gt; "Number is too small"