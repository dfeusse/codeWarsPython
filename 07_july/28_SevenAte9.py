'''
Write a function that removes each 9 that is surrounded by two 7s.

seven_ate9('79712312') =&gt; '7712312'
seven_ate9('79797') =&gt; '777'
'''
import re
def seven_ate9(string):
	remove = []
	for m in re.finditer('9', string):
		#print m.start(), m.end()
		print string[m.start()-1], string[m.end()]
		if string[m.start()-1] == '7' and string[m.end()] =='7':
			remove.append(string[m.start()-1])

		if len(remove) > 1:
			for i in remove:
				s = s[:pos] + s[(pos+1):]
		#if m[m.start()-1] == '7' and m[m.end] == '7':
		#	print 'AHHH'

print seven_ate9('79712312')
print seven_ate9('79797')


print '---------------------'

def multiple(x):
	if x % 3 == 0 and x % 15 == 0:
		return 'BangBoom'
	elif x % 5 == 0:
		return 'Boom'
	elif x % 3 == 0:
		return 'Bang'
	else:
		return 'Miss'

print (multiple(30), "BangBoom")
print (multiple(3), "Bang")
print (multiple(98),"Miss")
print (multiple(65),"Boom")
print (multiple(23),"Miss")
print (multiple(15),"BangBoom")