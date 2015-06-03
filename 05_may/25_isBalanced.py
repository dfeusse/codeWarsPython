'''
Given a string which may include opening or closing round brackets, can you tell whether the string 
contains a balanced pair(s) of round brackets, that is there are no brackets which are either opened 
& not closed, or vice versa. Opening round brackets always have to come before closing bracket. 
An empty string is balanced.
'''

def isBalanced(str):
	brackets = []
	for i in str:
		if i == '(':
			brackets.append(i)
		elif i == ')':
			if len(brackets) == 0:
				return False
			elif brackets[-1] == '(':
				del brackets[-1]
			else:
				return False
	if len(brackets) == 0:
		return True
	else:
		return False

print isBalanced("hi)(")
print isBalanced("hi(hi)")
print isBalanced("(")