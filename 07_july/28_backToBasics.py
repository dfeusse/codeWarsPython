'''
Create a program that will return whether an intered value is a str, int, float, or bool.
Return the name of the value.

Ex: Input = 23 --> Output = int Ex: Input = 2.3 --> Output = float 
Ex: Input = "Hello" --> Output = str Ex: Input = True --> Output = bool
'''	
def basics(inp):
	if isinstance(inp, str) == True:
		return 'str'
	elif isinstance(inp, int) == True:
		return 'int'
	elif isinstance(inp, float) == True:
		return 'float'
	else isinstance(inp, bool) == True:
		return 'bool'


#Input = 23 --> Output = int Ex: Input = 2.3 --> Output = float 
print basics("Hello") # --> Output = str Ex: Input = 
print basics(True) # --> Output = bool