'''
Create a find function that takes a string and an array. If the string is in the array, return true.

For example:

find("hello", ["bye bye","hello"]) # return true
find("anything", ["bye bye","hello"]) # return false
'''
def find(s, array):
	return True if s in array else False

print find("hello", ["bye bye","hello"]) # return true
print find("anything", ["bye bye","hello"]) # return false

'''
find=lambda x,y:x in y
'''