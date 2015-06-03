'''
There are two lists of different length. The first one consists of keys, 
the second one consists of values. Write a function createDict(keys, values) 
that returns a dictionary created from keys and values. If there are not enough 
values, the rest of keys should have a None (JS null)value. If there not enough 
keys, just ignore the rest of values.

Example 1:

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
Example 2:

keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
'''

def createDict(keys, values):
	return { a:b for a,b in map(None, keys, values[0:len(keys)])}

print createDict(['a','b','c'],[1,2,3,4])

'''
def createDict(keys, values):
    return dict(zip(keys, values)) if len(keys) < len(values) else dict(map(None, keys, values))

def createDict(keys, values):
    return dict(zip(keys, values + len(keys) * [None]))

def createDict(keys, values):
    return {k:(values[i] if i<len(values) else None) for i,k in enumerate(keys)}
'''

'''
>>> keys = ['a', 'b', 'c']
>>> values = [1, 2, 3]
>>> dictionary = dict(zip(keys, values))
>>> print dictionary
{'a': 1, 'b': 2, 'c': 3}
'''