'''
Return the array/list passed into the function with all duplicates removed.

The items in the returned array should be sorted alphabetically, with numbers before strings. 
The function should remove any null, undefined and invalid values from the array 
If the variable is not an array/list, the function should return a string Not an array
'''
def noDups(arr):
	newArray = []
	if isinstance(arr, list) != True:
		return "Not an array"
	else:
		for i in arr:
			if i not in newArray or i is None:
				newArray.append(i)
	return sorted(newArray)

print noDups([1,2,3,"dan","pone"])
print noDups([1,2,3,"dan","pone",2,5])