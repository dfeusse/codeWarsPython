'''
flatten out a list
'''
def flatten(lists):
	newList = []
	for i in lists:
		newList.append(i)
	return newList

print flatten(['a', ['b', 'd']])