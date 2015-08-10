'''
Create a program that will return whether an intered value is a str, int, float, or bool. 
Return the name of the value.

Ex: Input = 23 --> Output = int 
Ex: Input = 2.3 --> Output = float 
Ex: Input = "Hello" --> Output = str 
Ex: Input = True --> Output = bool
'''
def back(x):
	return "%s" % {str:"str", float:"float", int:"int", bool:"bool"}.get(type(x))

print back(23)
print back(2.3)
print back('Hello')
print back(True)


'''
def types(x):
    return type(x).__name__

def types(x):
    for (i,t) in enumerate([bool,str,int,float]):
        if isinstance(x,t):
            return ("bool","str","int","float")[i]

'''