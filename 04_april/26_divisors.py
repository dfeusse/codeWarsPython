'''
Find the number of divisors of a positive integer n.

Example:

divisors(4) -&gt; 3 -- 1, 2, 4
divisors(5) -&gt; 2 -- 1, 5
divisors(12) -&gt; 6 -- 1, 2, 3, 4, 6, 12
divisors(30) -&gt; 8 -- 1, 2, 3, 5, 6, 10, 15, 30
'''

'''
def divisors(num):
	divisors = []
	for i in range(1,num+1):
		if num % i == 0:
			divisors.append(i)
	return divisors

print divisors(10)
'''

def divisors(num):
	return len([ x for x in range(1,num+1) if num % x == 0 ])
	'''	
		With a filter, you need:
			[ EXP for x in seq if COND ]
			like above
		Without a filter you need:
			[ EXP for x in seq ]
			[ x if x%2 else x*100 for x in range(1, 10) ]
	'''
	
print divisors(10)


'''
def divisors(n):
    return len([d for d in range(1, n+1) if n % d == 0])

def divisors(n):
    if n==1: return 1
    t = 2
    for i in range(2,n/2+1): t += 0 if n%i else 1
    return t
'''