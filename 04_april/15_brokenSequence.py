'''
You have a sequence of positive numbers starting with 1, but one number is missing!

Find out the missing number; if the sequence is not broken, you should return 0. Each sequence always increments by 1.

In short: an invalid sequence must return 1, an already complete sequence must return 0; otherwise return the missing element.

Note that the sequence may be shuffled.

E.g.

find_missing_number("1 2 3 5") # returns 4
find_missing_number("1 2 3 4") # returns 0
find_missing_number("5 1 3 4") # returns 2
'''

def find_missing_number(sequence):
	if sequence == "":
		return 0
	else:
		number = sequence.replace(" ","")
		sortedNum = ''.join(sorted(number))
		expectedNum = range(int(sortedNum[0]), int(sortedNum[-1])+1)		
		# returns [1, 2, 3, 4, 5, 6], need to condense to '123456'
		expectedNumStr = ''
		for n in expectedNum:
			expectedNumStr = expectedNumStr + str(n)

		if sortedNum == expectedNumStr:
			return 0
		else:
			missingNumber = ''
			# loop through both lists
			# [ xy.append(a*b) for a, b in map(None, x, y) ]
			for a, b in map(None, sortedNum, expectedNumStr):
				if a != b:
					missingNumber = a
			return missingNumber

print find_missing_number("")
print find_missing_number("6 1 4 3 2")
print find_missing_number("6 5 1 4 3 2")