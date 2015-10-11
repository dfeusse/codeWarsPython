'''
which checks if a given number n can be written as the sum of two cubes in two different ways: 
n = a^3+b^3 = c^3+d^3. All the numbers a, b, c and d should be different and greater than 0.

E.g. 1729 = 9^3+10^3 = 1^3+12^3.

has_two_cube_sums(1729); // true
has_two_cube_sums(42);   // false
'''
def has_two_cube_sums(n):
	nums = [int(x) for x in str(n)]
	if any(nums.count(x) > 1 or x<1 for x in nums):
		return False

# maybe can cube all, sort them, add first and last and middle two

print has_two_cube_sums(1729); #// true
print has_two_cube_sums(42);   #// false