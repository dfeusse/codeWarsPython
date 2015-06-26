'''
Create a function isDivisible(n,x,y) that checks if a number n is divisible by two numbers x AND y

Example:
is_divisible(3,1,3)--&gt; true because 3 is divisible by 1 and 3
is_divisible(12,2,6)--&gt; true because 12 is divisible by 2 and 6
is_divisible(100,5,3)--&gt; false because 100 is not divisible by 3
is_divisible(12,7,5)--&gt; false because 12 is neither divisible by 7 nor 5
'''
def is_divisible(num, a, b):
	return True if num % a == 0 and num % b == 0 else False

print is_divisible(3,1,3) #--&gt; true because 3 is divisible by 1 and 3
print is_divisible(12,2,6) #--&gt; true because 12 is divisible by 2 and 6
print is_divisible(100,5,3) #--&gt; false because 100 is not divisible by 3
print is_divisible(12,7,5) # false

'''
is_divisible=lambda n,x,y: n%x==0 and n%y==0
'''