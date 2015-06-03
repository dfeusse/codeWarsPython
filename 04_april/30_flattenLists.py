'''
Flattening Lists

In this Kata you will create a function that takes a 
list of lists as an input and returns a flat list.

Example:

flatten [[1,2],[3,4]] == [1,2,3,4]
flatten [[1],[2],[3],[4]] == [1,2,3,4]
'''

def flatten(lists):
	newlist = []
	for i in lists:
		for p in i:
			newlist.append(p)
	return newlist

print flatten([[1,2],[3,4]])
print flatten([[1],[2],[3],[4]]) 

'''
def flatten(list):
  return [item for sublist in list for item in sublist]

def flatten(lists):
    flat_list = []
    for list in lists:
        flat_list += list
    return flat_list
'''