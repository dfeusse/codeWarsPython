'''
Write a reverseWords function that accepts a string a parameter, 
and reverses each word in the string. Every space should stay, 
so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"
'''
def reverse_words(string):
	#for i in string:
	newarray = []
	for i in string.split(' '):
		newarray.append(i[::-1])
		#return string[::-1]
	return ' '.join(newarray)


def reverse_words(string):
	return ' '.join([ i[::-1] for i in string.split(' ') ])

print reverse_words("This is an example!")

'''
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

import re
def reverse_words(str):
  return ''.join(word[::-1] for word in re.split(r'(\s+)', str))
'''