'''
SevenAte9

Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') =&gt; '7712312'
seven_ate9('79797') =&gt; '777'
'''
def seven_ate9(string):
	nums = [ int(s) for s in string ]
	i = 1
	for z in nums[1:len(string)-1]:
		if nums[i-1] == 7 and nums[i+1] == 7:
			print z
	return nums

print seven_ate9('79712312')# =&gt; '7712312'
print seven_ate9('79797')# =&gt; '777'