'''
"Any word or phrase that exactly reproduces the letters in another order is an anagram." 
(Wikipedia). Add numbers to this definition to be more interest.

Examples of anagrams:

William Shakespeare = I am a weakish speller
silent = listen
12345 = 54321
'''

def anagram(original, test):
	'''
	if ''.join(sorted(original.replace(" ","").lower())) == ''.join(sorted(test.replace(" ","").lower())):
		return True
	else:
		return False
	'''
	return True if ''.join(sorted(original.replace(" ","").lower())) == ''.join(sorted(test.replace(" ","").lower())) else False

print anagram('William Shakespeare', 'I am a weakish speller')
print anagram('silent', 'listen')
print anagram('12345', '54321')
print anagram('', '54321')