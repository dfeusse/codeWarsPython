'''
List length v2

Like my last kata, try to make a function that counts the length of a list, but this time, 
without any of the default len functions, which are removed.

In this example, the for loop is quite important. Here is an example of looping through a list:

for character in thelist:
  # do something...
'''
def listLen(l):
	length = 0
	for i in l:
		length += 1
	return length

'''
def count(lst):
  return sum(1 for _ in lst)

def count(lst):
    t = 0
    for c in lst: t = t + 1
    return t

 def count(lst):
    return 0 if lst == [] else 1 + count(lst[1:])
'''