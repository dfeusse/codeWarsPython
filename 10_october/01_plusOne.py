'''
Given an array of integers of any length, return an array that has 1 added to the value 
represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

The array can't be empty and only positive, single digit integers are allowed. The function should return 
null if the array is empty or any of the array values are negative or more than 10.

[1, -9] would return null/nil/None (according to the language implemented).
'''
def plusOne(arr):
	#return None for i in arr if i < 0
	for i in arr:
		if i < 1: return None
	#return map(int, str(int(''.join(map(str, arr))) + 1))
	daria = int(''.join(str(z) for z in arr))
	print daria

print plusOne([2, 3, 9])
print plusOne([4, 3, 2, 5])
print plusOne([1, -9])