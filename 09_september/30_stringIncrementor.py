'''
Your job is to write a function which increments a string, to create a new string. 
If the string already ends with a number, the number should be incremented by 1. 
If the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''
def inc(s):
	head = s.rstrip('0123456789')
	tail = s[len(head):]
	print head, tail
	print '----------'
 
#[mysplit(s) for s in ['foofo21', 'bar432', 'foobar12345']]

print inc('foo') #-> foo1
print inc('foobar23') #-> foobar24
'''
print inc('foo0042') #-> foo0043
print inc('foo9') #-> foo10
print inc('foo099') #-> foo100
'''