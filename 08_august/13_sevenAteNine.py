'''
Write a function that removes each 9 that is surrounded by two 7s.
seven_ate9('79712312') =&gt; '7712312'
seven_ate9('79797') =&gt; '777'
'''
def seven_ate9(s):
	for i in range(len(s)):
		newPone = s.find('797')
		print s[:newPone+1] + s[newPone+2:]

print seven_ate9('2279712312')# =&gt; '7712312'
print seven_ate9('79797') #=&gt; '777'