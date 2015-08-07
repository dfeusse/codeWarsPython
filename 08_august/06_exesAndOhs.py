'''
Check to see if a string has the same amount of 'x's and 'o's and return true otherwise false. 
If the string doesn't contain an 'x' or an 'o', return true. E.g 'abc' doesn't contain any x's or o's. 
However, "xxxm" does contain x's but it doesn't have an equal amount of o's, hence false is expected. 
The same goes with 'ooom', solution should return false. 
The solution must be case-insensitive.
'''
def exes(s):
	return True if s.count('x') == s.count('o') else False

'''
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
'''