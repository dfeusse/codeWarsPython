'''
Given an integer as input, can you round it to the next 5?

Examples:

input:    output:
0    -&gt;   0
2    -&gt;   5
3    -&gt;   5
12   -&gt;   15
21   -&gt;   25
30   -&gt;   30
etc.
'''
def roundUp(n):
	while n % 5 != 0:
		n = n + 1
	return n

print roundUp(6)

'''
def round_to_next5(n):
    # Your code here
    rem = n % 5
    return n + ((5 - rem) if rem else 0)

def round_to_next5(n):
    return 5 * ((n+4)/5)
'''