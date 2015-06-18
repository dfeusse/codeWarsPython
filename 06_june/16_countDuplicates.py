'''
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters that 
occur more than once in the given string. The given string can be assumed to contain only uppercase 
and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
'''
def duplicates(text):
	dups = []
	letters = []
	for i in text.lower():
		if i not in letters:
			letters.append(i)
		else:
			if i not in dups:
				dups.append(i)
	return len(dups)

print duplicates("abcde") #-> 0 # no characters repeats more than once
print duplicates("aabbcde") #-> 2 # 'a' and 'b'
print duplicates("aabbcdeB") #-> 2 # 'a' and 'b'
print duplicates("indivisibility") #-> 1 # 'i'
print duplicates("Indivisibilities") #-> 2 # 'i' and 's'