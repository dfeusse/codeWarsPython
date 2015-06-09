'''
A palindrome is a string which reads the same forward and backward. 
It can be a word or a sentence. Examples are:

abba
Mom!
Dad?
If I had a hi-fi...
Create a function which determines for a given string if it's a palidrome or not. 
For this task the following properties must be fulfilled:

return a boolean value
consider an empty string as a legal word
ignore case
ignore whitespace and punctuation
'''
import string

def palindrome(word):
	newWord = word.replace(" ","").lower().translate(None, string.punctuation)
	return True if newWord == newWord[::-1] else False


print palindrome('abba')
print palindrome('Mom!')
print palindrome('Dad?')
print palindrome('If I had a hi fi')

'''
def is_palindrome(string):
    string = ''.join(s for s in string.lower() if s.isalnum())
    return string[::-1] == string

def is_palindrome(s):
    testStr = [ x.lower() for x in s if x.isalnum() ]
    
    return testStr[::-1] == testStr
'''