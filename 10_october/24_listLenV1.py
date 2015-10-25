'''
Try to make a function that counts the length of a list, without the len function, which is removed. 
Should be quite simple, but this is my first Kata!

In this example, the for loop can be quite important. Here is an example of looping through a string:
'''
def count(lst):
	i = 0
	for z in lst:
		i+=1
	return i

'''
def count(lst):
    return sum([1 for i in lst])
'''