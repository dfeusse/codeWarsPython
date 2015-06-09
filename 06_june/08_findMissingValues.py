'''
You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.

In short: an invalid sequence must return 1, an already complete (or empty) sequence must return 0; otherwise return the missing element.

Note that the sequence may be shuffled.

E.g.

find_missing_number("1 2 3 5") # returns 4
find_missing_number("1 2 3 4") # returns 0
find_missing_number("5 1 3 4") # returns 2
'''
def find_missing_number(string):
	given = sorted(map(int, string.split(' ')))
	ideal = range(1,sorted(map(int, string.split(' ')))[-1]+1)
	# compare each element of both lists
	if given == ideal:
		return 0
	else:
		return list(set(given)^set(ideal))[0]



print find_missing_number("1 2 3 5") # returns 4
print find_missing_number("1 2 3 4") # returns 0
print find_missing_number("5 1 3 4") # returns 2