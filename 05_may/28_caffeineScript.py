'''
Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".

If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"
'''

def caffeineBuzz(integer):
	if (integer % 3 == 0 and integer % 4 == 0):
		if integer % 2:
			return 'CoffeeScript'
		else:
			return 'Coffee'
	elif integer % 3:
		if integer % 2:
			return 'JavaScript'
		else:
			return 'Java'
	else:
		return "mocha_missing"

print caffeineBuzz(1)
print caffeineBuzz(9)
print caffeineBuzz(12)