'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office 
standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" 
ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and 
sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.

Examples:

### Python ###

tickets([25, 25, 50]) # =&gt; YES 
tickets([25, 100]) # =&gt; NO. Vasya will not have enough money to give change to 100 dollars
'''
def tickets(tckts):
	registerCash = 0
	for i in tckts:
		registerCash = registerCash + 25
		change = i - 25
		if registerCash < change:
			return 'NO'
	return 'YES'




print tickets([25, 25, 50]) # =&gt; YES 
print tickets([25, 100]) 