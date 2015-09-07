'''
Error Handling is very important in coding. Most error handling seems to be overlooked or not implemented properly.
Task

Your task is to implement a function which is expected to take a string and return an object containing the properties vowels and consonants The vowels property must contain the total count of vowels (y in this case is not a vowel), and consonants are anything else, you must also trim any spaces. Don't forget to handle invalid input but also returning valid input.

Example:

Input: get_count('test')
Output: {vowels:1,consonants:3}

Input: get_count('tEst')
Output: {vowels:1,consonants:3}

Input get_count('    ')
Output: {vowels:0,consonants:0}

Input get_count()
Output: {vowels:0,consonants:0}
'''
def get_count(s):
	try:
		print s
	except TypeError:
		print 'an error'
		d = {vowels:0,consonants:0}
		return d

print get_count('test')
print get_count('tEst')
print get_count('    ')
print get_count()
