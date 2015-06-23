'''
Given a non-negative integer, return an array containing a list of independent digits in reverse order.

Example:

348597 => [7,9,5,8,4,3]
'''
def reverseArray(nums):
	return [int(i) for i in str(nums)][::-1]

print reverseArray(348597) # [7,9,5,8,4,3]

'''
def digitize(n):
    return [int(x) for x in str(n)[::-1]]

def digitize(n):
    return map(int, str(n)[::-1])

'''