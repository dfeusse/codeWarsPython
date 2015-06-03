'''
An isogram is a word that has no repeating letters, consecutive 
or non-consecutive. Implement a function that determines whether 
a string that contains only letters is an isogram. Assume the empty 
string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

def is_isogram(string):
	new = ''.join(sorted(string)).lower()
	return True if len(set(new)) == len(new) else False

print is_isogram("Dermatoglyphics" )
print is_isogram("aba" )
print is_isogram("moOse" )

'''
def is_isogram(string):
    return len(string) == len(set(string.lower()))

def is_isogram(string):
    s = string.lower()
    return len(s) == len(set(s))
'''