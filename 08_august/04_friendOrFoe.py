'''
Make a program that filters a list of strings and returns a list with only your friends name in it. 
All your friends only have four letter in their name.

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
'''
def friend(l):
	return [i for i in l if len(i) == 4]

print friend(["Ryan", "Kieran", "Jason", "Yous"])

'''
def friend(x):
    return [f for f in x if len(f) == 4]

def friend(x):
    return filter(lambda name: len(name) == 4, x)
    '''