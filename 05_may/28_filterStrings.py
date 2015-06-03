'''
In this kata you will create a function that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.

Example

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

def filter_list(array):
	# type() is terrible in python when checking for strings
	# use isinstance(target, str)
	newarray = []
	for i in array:
		if isinstance(i, int):
			newarray.append(i)
	return newarray

def filter_list_two(array):
	return [i for i in array if isinstance(i, int)]

print filter_list([1,2,'a','b'])# == [1,2]
print filter_list([1,'a','b',0,15])# == [1,0,15]
print filter_list([1,2,'aasf','1','123',123])# == [1,2,123]

print filter_list_two([1,2,'a','b'])# == [1,2]
print filter_list_two([1,'a','b',0,15])# == [1,0,15]
print filter_list_two([1,2,'aasf','1','123',123])# == [1,2,123]

'''
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

def filter_list(l):
  return filter(lambda x: not type(x) is str, l)

def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]
'''