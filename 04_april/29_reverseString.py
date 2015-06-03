'''
Complete the solution so that it reverses the string 
value passed into it.

solution('world') # returns 'dlrow'
'''

def solution(string):
	newStr = ''
	for i in string[::-1]:
		newStr = newStr + i
	return newStr
		

print solution('dan')

'''
def solution(str):
  	return str[::-1]

def solution(s):
    return ''.join(reversed(s))

solution = lambda s: s[::-1]

def solution(str):
    newstring = []
    for char in reversed(str):
      newstring.append(char)
      
    return ''.join(newstring)

'''