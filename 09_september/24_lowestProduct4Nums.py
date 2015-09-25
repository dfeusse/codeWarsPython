'''
Lowest product of 4 consecutive numbers

Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers.

This should only work is the number has 4 digits of more. If not, return "Number is too small".

Example

lowest_product("123456789")--&gt; 24 (1x2x3x4)
lowest_product("35") --&gt; "Number is too small"
'''
def lowest_product(s):
    if len(s) < 4:
        return "Number is too small"
    else:
        nums = [int(s) for s in str(s)]
        small = 10000000
        i = -1
        for a in nums:
			i += 1
			if len(nums) - nums[i] > 3:
				print a
				print nums[i]
				product = nums[i] * nums[i+1] * nums[i+2] * nums[i+3]
				print product
				if product < small:
					small = product
	return small

print(lowest_product("123456789"))#,24); 
print(lowest_product("2345611117899"))#,1);
print(lowest_product("2305611117899"))#,0);
print(lowest_product("333"))#,"Number is too small");
print(lowest_product("1234111"))#,4,"Numbers should be consecutives");