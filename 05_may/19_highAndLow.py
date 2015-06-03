'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def highlow(str):
	sortedStrList = sorted(str.split(), key=int)
	first = sortedStrList[0]
	last = sortedStrList[-1]
	return int(first),int(last)

print highlow('1 9 3 12 16 8 999 2')

'''
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
    nums = map(int, numbers.split(" "))
    return " " .join(map(str, (max(nums), min(nums))))
'''