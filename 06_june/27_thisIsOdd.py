'''
Create a function that checks if a number is odd.

Expect negative and decimal numbers too. For negative numbers, return true if its 
absolute value is odd. For decimal numbers, return true only if the number is equal 
to its integer part and the integer part is odd.

Examples

Example:
is_odd(2)--&gt; false
is_odd(5)--&gt; true
is_odd(4)--&gt; false
is_odd(-17)--&gt; true
is_odd(-7.0)--&gt; true
is_odd(-7.1)--&gt; false
is_odd(4.23)--&gt; false
'''
def is_odd(n):
	if isinstance(n, float) == True:
		return True if (abs(n)-1) % 2 == 0 else False
	return True if abs(n) % 2 != 0 else False

print is_odd(2)#--&gt; false
print is_odd(5)#--&gt; true
print is_odd(4)#--&gt; false
print is_odd(-17)#--&gt; true
print is_odd(-7.0)#--&gt; true
print is_odd(-7.1)#--&gt; false
print is_odd(4.23)#--&gt; false
print is_odd(-16)#--&gt; false
print is_odd(-7.0)#--&gt; true

'''
def is_odd(n):
    return n%2==1 
    
def is_odd(n):
    return n == round(n) and abs(n) % 2 != 0
'''