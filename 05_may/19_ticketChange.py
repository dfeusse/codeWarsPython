'''
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to cell a ticket to every single person in this line.

Can Vasya cell a ticket to each person and give the change if he initially has no money and cells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can cell a ticket to each person and give the change. Otherwise return NO.

Examples:

### Python ###

tickets([25, 25, 50]) # =&gt; YES 
tickets([25, 100]) # =&gt; NO.
'''

def tickets(tickets):
	rev = 0
	for i in tickets:
		moneyNeedForChange = i - 25
		if rev < moneyNeedForChange:
			return 'NO'
		else:
			rev - moneyNeedForChange
		rev += 25
	return 'YES'

print tickets([25, 25, 50]) # =&gt; YES 
print tickets([25, 100]) #NO