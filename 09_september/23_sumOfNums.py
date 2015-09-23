'''
Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!

Example: 
get_sum(1, 0) == 1
get_sum(1, 2) == 3
get_sum(0, 1) == 1
get_sum(1, 1) == 1
get_sum(-1, 0) == -1
'''
def get_sum(a,b):
	return sum(range(b,a+1)) if a > b else sum(range(a,b+1))

print get_sum(1, 0)# == 1
print get_sum(1, 2) #== 3
print get_sum(0, 1) #== 1
print get_sum(1, 1) #== 1
print get_sum(-1, 0)# == -1

'''
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
'''