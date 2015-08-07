'''
Your job is to write a function which increments a string, to create a new string.
 If the string already ends with a number, the number should be incremented by 1. 
 If the string does not end with a number the number 1 should be appended to the new string.

foo -&gt; foo1

foobar23 -&gt; foobar24

foo0042 -&gt; foo0043

foo9 -&gt; foo10

foo099 -&gt; foo100
'''
import re
def stringInc(s):
	p = filter(None, re.split('(\D+)', s))
	return p[0]+str(int(p[1].rstrip("0"))+1) if len(p) > 1 else p[0] + '1'

print stringInc('foo') # -&gt; foo1
print stringInc('foobar23') #-&gt; #foobar24
print stringInc('foo0042')# -&gt; foo0043
print stringInc('foo9') # -&gt; foo10
print stringInc('foo0990') #-&gt; foo100