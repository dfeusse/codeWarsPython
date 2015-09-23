'''
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates 
and the paperwork has 'm' pages.

Your task is to calculate how much blank pages do you need.

Example:
paperwork(5, 5) == 25
Note! if n or m < 0 return 0! Waiting for translations and Feedback! Thanks!
'''
def paperwork(n, m):
	return 0 if n < 0 or m < 0 else m*n

print paperwork(5, 5)

'''
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0

paperwork = lambda m, n: 0 if (m <= 0 or n <= 0) else m * n
'''