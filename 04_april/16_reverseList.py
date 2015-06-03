'''
In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples

reverse_list([1,2,3,4]) == [4,3,2,1]
reverse_list([3,1,5,4]) == [4,5,1,3]
'''

def reverse_list(l):
	newList = []
	for i in reversed(l):
		newList.append(i)
	return newList

'''
def reverse_list(l):
  return l[::-1]

def reverse_list(l):
  """return a list with the reverse order of l"""
  return list(reversed(l))
'''