'''
Implement the function unique_in_order which takes as argument a sequence and returns a 
list of items without any elements with the same value next to each other and preserving 
the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''
def unique_in_order(text):
	newlist = []
	previous = ''
	for i in text:
		if i != previous:
			newlist.append(i)
		previous = i
	return newlist

print unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
print unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
print unique_in_order([1,2,2,3,3])       == [1,2,3]

'''
def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
'''