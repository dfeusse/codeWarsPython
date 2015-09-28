'''
Finish the solvePostfix function. The input will be a postfix string and for ease the character 
will be seperated by a space. The function should return a Number. The solvePostfix function with 
the input string 12 4 * 2 ^ 5 + Should return 2309. Operators Types = (^,*,/,+,-). For more information 
on how to solve RPN read Reverse Polish Notation on wikipedia.

*Once you have finished this one try the harder version 
http://www.codewars.com/kata/reverse-polish-notation-calculator/javascript

Note: for simplicity's sake, assume that the "/" operator behaves like it usually does in the chosen 
language: float division in JS, integer division in both Ruby and Python 2 (the defaul Python on this site).
'''
def solve_postfix(pfx):
	'''for i in pfx.split()[2:]:
		print i
	'''
	return int(pfx.split()[0]) + int(pfx.split()[1])

print(solve_postfix("2 3 +"))#,5)
print(solve_postfix("2 8 -"))#,-6)
print(solve_postfix("4 2 /"))#,2)
print(solve_postfix("10 5 / 7 + 3 ^ 10 -"))#,719)
