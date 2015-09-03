'''
You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence 
always increments by 1.

In short: an invalid sequence must return 1, an already complete (or empty) sequence must 
return 0; otherwise return the missing element.

Note that the sequence may be shuffled.
'''
def find_missing_number(s):
	li = sorted([ int(i) for i in s.split() ])
	new = range(1,li[-1]+1)
	for a,b in zip(li, new):
		if a != b:
			return min(a,b)
	return 0

print find_missing_number("1 2 3 5") # returns 4
print find_missing_number("1 2 3 4") # returns 0
print find_missing_number("5 1 3 4") # returns 2