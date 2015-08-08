'''
Given an array of integers of any length, return an array that has 1 added to the value 
represented by the array.

For example an array [2, 3, 9] equals 239, add one would return an array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

The array can't be empty and only positive, single digit integers are allowed. The function 
should return null if the array is empty or any of the array values are negative or more than 10.

[1, -9] would return null/nil/None (according to the language implemented).
'''
def plusOne(numList):
	#return [i for i in arr]
    num = int(''.join(map(str, numList))) + 1
    return map(int, str(num))

print plusOne([2, 3, 9]) # [2, 4, 0])
print plusOne([4, 3, 2, 5]) # [4, 3, 2, 6])