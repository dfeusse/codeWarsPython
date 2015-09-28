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
import operator
def solve_postfix(pfx):
	'''
	print pfx.split()[3:][::2]
	print pfx.split()[4:][::2]
	print zip(pfx.split()[4:][::2], pfx.split()[3:][::2])
	'''
	wholeList = pfx.split()
	ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.div, '%' : operator.mod,'^' : operator.xor}
	#return int(pfx.split()[0]) + ops[pfx.split()[2]] + int(pfx.split()[1])
	if len(wholeList) > 3:
		initial = ops[pfx.split()[2]](int(pfx.split()[0]),int(pfx.split()[1]))
		array = zip(pfx.split()[4:][::2], pfx.split()[3:][::2])
		for i in array:
			print i[0]
			print i[1]
			initial = ops[i[0]](initial, int(i[1]))
			print initial
		return initial
	else:
		return ops[pfx.split()[2]](int(pfx.split()[0]),int(pfx.split()[1]))
	

print(solve_postfix("2 3 +"))#,5)
print(solve_postfix("2 8 -"))#,-6)
print(solve_postfix("4 2 /"))#,2)
print(solve_postfix("10 5 / 7 + 3 ^ 10 -"))#,719)
