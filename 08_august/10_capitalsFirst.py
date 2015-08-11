'''
Beta
Capitals first!

Create a function that takes an input String and returns a String, 
where all the uppercase words of the input String are in front and all the lowercase words at the end.

If a word starts with a number or special character, skip the word and leave it out of the result.

Input String will not be empty.

For an input String: "hey You, Sort me Already!" the function should return: "You, Sort Already! hey me"
'''
def capitals(s):
	uppers = ""
	lowers = ""
	new = s.split()
	for i in new:
		if i[0].isupper():
			uppers = uppers + " " + i
		elif i[0].isalpha():
			lowers = lowers + " " + i
	return (uppers + lowers).strip()

print capitals("hey You, Sort me Already!") # "You, Sort Already! hey me"