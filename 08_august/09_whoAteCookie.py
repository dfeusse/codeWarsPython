'''
For this problem you must create a program that says who ate the last cookie. 
If the input is a string then "Zach" ate the cookie. 
If the input is a float or an int then "Monica" ate the cookie. 
If the input is anything else "the dog" ate the cookie. 
The way to return the statement is: "Who ate the last cookie? It was (name)!"
'''
def cookie(inp):
	if isinstance(inp, str):
		return "Who ate the last cookie? It was Zach!"
	elif isinstance(inp, float) or type(inp) == int:
		return "Who ate the last cookie? It was Monica!"
	else:
		return "Who ate the last cookie? It was the dog!"

print cookie("Ryan")#, "Who ate the last cookie? It was Zach!")
print cookie(2.3)#, "Who ate the last cookie? It was Monica!")
print cookie(26)#, "Who ate the last cookie? It was Monica!")
print cookie(True)

'''
def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

def cookie(x):
    try:
        who = {int: 'Monica', float: 'Monica', str: 'Zach'}[type(x)]
    except KeyError:
        who = 'the dog'
    return 'Who ate the last cookie? It was %s!' % who
 '''