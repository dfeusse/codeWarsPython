'''
Return the array/list passed into the function with all duplicates removed.

The items in the returned array should be sorted alphabetically, with numbers 
before strings.

The function should remove any null, undefined and invalid values 
from the array (in JS: all falsey values (NaN, false, undefined, null etc.)
 have to be removed). If the variable is not an array/list, the function 
should return a string, Not an array
'''
def noDups(arr):
	if isinstance(arr, list):
		newArray = []
		for i in arr:
			print i
			if i not in newArray and i != None:
				newArray.append(i)
		return sorted(newArray)
		#return sorted([i for i in arr if i.count(i) == 1 and i != None])
	else:
		return "Not an array"

print noDups(['dan', 1, 'dan', 10, 'emma'])