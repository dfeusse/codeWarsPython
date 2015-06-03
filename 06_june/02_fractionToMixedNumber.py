'''
Given a string representing a simple fraction x/y, your function must return a string 
representing the corresponding mixed fraction in the following format:

a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space 
between a and b/c.

If the x/y equals the integer part, return integer part only. If integer part is zero, return the 
irreducible proper fraction only.

Division by zero should return the standard zero division error.

Examples

Input: 42/9, expected result: 4 2/3.
Input: 6/3, expedted result: 2.
Input: 4/6, expected result: 2/3.
Input: 0/18891, expected result: 0.
Input: -10/7, expected result: -1 3/7.
Inputs 0/0 or 3/0 must raise a zero division error.
'''
import math

def fractionToMN(fraction):
	nums = fraction.split('/')
	#big = math.ceil(float(nums[0]) / int(nums[1]))
	if int(nums[0])/int(nums[1]) < 0:
		big = math.ceil(float(nums[0]) / int(nums[1]))
	else:
		big = int(nums[0]) / int(nums[1])
		rem = int(nums[0]) % int(nums[1])
	return big

print fractionToMN('42/9')#, expected result: 4 2/3.
print fractionToMN('6/3')#, expedted result: 2.
print fractionToMN('4/6')#, expected result: 2/3.
print fractionToMN('0/18891')#, expected result: 0.
print fractionToMN('-10/7')#, expected result: -1 3/7.
#print fractionToMN('0/0') # 
#print fractionToMN('3/0') #must raise a zero division error.