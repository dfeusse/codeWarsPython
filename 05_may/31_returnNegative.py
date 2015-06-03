'''In this simple assignment you are given a number and have to make it negative. 
But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes:

The number can be negative already, in which case no change is required.
Zero (0) can't be negative, see examples above.
'''

'''
def make_negative(integer):
	if integer > 0:
		return -abs(integer)
	else:
		return integer
'''
def make_negative(integer):
	return -abs(integer) if integer > 0 else integer

print make_negative(1);  # return -1
print make_negative(-5); # return -5
print make_negative(0);  # return 0

'''
def make_negative( number ):
    return -abs(number)

def make_negative( number ) :#z.
    return -number if number > 0 else number
'''