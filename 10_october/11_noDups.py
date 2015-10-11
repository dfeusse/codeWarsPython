'''
Return the array/list passed into the function with all duplicates removed.

The items in the returned array should be sorted alphabetically, with numbers before strings.

The function should remove any null, undefined and invalid values from the array (in JS: all 
falsey values (NaN, false, undefined, null etc.) have to be removed). If the variable is not an array/list, 
the function should return a string Not an array

'''
def list_de_dup(arr):
    newArray = []
    if isinstance(arr, list) != True:
		return "Not an array"
    else:
		for i in arr:
			if i not in newArray and i != None:
			    newArray.append(i)
    return sorted(newArray)

listy = ["g", 3, "a", "a"]
print(list_de_dup(listy))#, [ 3, 'a', 'g' ])
listy = [1, 2, 3, 4, 1, 2, 3, 4]
print(list_de_dup(listy))#, [1, 2, 3, 4])
listy = ["code", "wars", "ain't", None, None, "code", "wars", "ain't","the","same","as","the","rest"]
print(list_de_dup(listy))#, ['ain\'t', 'as', 'code', 'rest', 'same', 'the', 'wars'])

'''
def exists(it):
    return it is not None

def list_de_dup(list_):
  if type(list_) != list: return 'Not an array'
  return sorted( list( set(filter(exists, list_)) ))
  '''