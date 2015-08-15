'''
In Your class You have started lessons about Geometric Progression Because You are also a programmer, 
You have decided to write a function geometric_sequence_sum(a, r, n) 
that will print SUM of the first n elementh of the sequence with the given constant r and 
first elementh a

For example geometric_sequence_sum(2, 3, 5)
Should return: 242
'''
def geometric_sequence_sum(a, r, n):
	# 2 + 2*3 + 2*3*3 + 2*3*3*3*3
	nums = []
	for i in range(n):
		nums.append(3**i * 2)
	return sum(nums)
'''
def geometric_sequence_sum(a, r, n):
	# 2 + 2*3 + 2*3*3 + 2*3*3*3*3
	return sum([ r**i*2 for i in range(n) ])
'''

print geometric_sequence_sum(2, 3, 5)#, 242)
print geometric_sequence_sum(1, 1, 2)#, 2)
print geometric_sequence_sum(2, 2, 10)#, 2046)
print geometric_sequence_sum(1, -2, 10)#, -341)
print geometric_sequence_sum(1, 0.5, 10)#, 1.998046875)