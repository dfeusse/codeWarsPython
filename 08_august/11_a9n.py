'''
The word i18n is a common abbreviation of internationalization the developer community 
use instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an 
abbreviation of accessibility.

Write a function that takes a string and turns any and all words within that string of 
length 4 or greater into an abbreviation following the same rules.

Notes:

A "word" is a sequence of alphabetical characters. By this definition, if there is a hyphen 
(eg. "elephant-ride"), this will produce two, one on either side (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, 
then the last letter (eg. "e6t-r2e").
'''
def abbrev(s):
	if len(s) > 3:
		s = s.split("-")
		for i in s:
			print i[0] + str(len(i[1:len(i)-1])) + i[-1]
	else:
		return s

def abbrev(s):
	if len(s) > 3:
		return ' '.join([ i[0] + str(len(i[1:len(i)-1])) + i[-1] for i in s.split("-") ])
	else:
		return s

def abbrev(s):
	return ' '.join([ i[0] + str(len(i[1:len(i)-1])) + i[-1] for i in s.split("-") ]) if len(s) > 3 else s

print abbrev("elephant-ride")
print abbrev("danny")
print abbrev("sits-doggy")