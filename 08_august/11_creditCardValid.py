'''
Credit Card Validifier

Make a program that sees if a credit card number is valid or not. 
Also the program should tell you what type of credit card it is if it is valid.

The five things you should consider in your program is: AMEX, Discover, VISA, Master, and Invalid

Discover starts with 6011 and has 16 digits, 
AMEX starts with 34 or 37 and has 15, 
Master Card starts with 51-55 and has 16, 
VISA starts with 4 and has 13 or 16 digits.

Ex: Input: 6011364837263748 --> Output: "Discover" Ex: Input: 5318273647283745 --> Output: "Master" 
Ex: Input: 12345678910 --> Output: "Invalid" Ex: Input: 37123647382367 --> Output: "AMEX" 
Ex: Input: 4128374839283 --> Output: "VISA"
'''
def ccValid(card):
	# AMEX
	if (str(card)[:2] == '34' or str(card)[:2] == '37') and len(str(card)) == 15:
		return 'AMEX'
	# Discover
	elif str(card)[:4] == '6011' and len(str(card)) == 16:
		return 'Discover'
	# VISA
	elif str(card)[:1] == '4' and (len(str(card)) == 13 or len(str(card)) == 16):
		return 'VISA'
	# Master
	elif (str(card)[:2] == '51' or '52' or '53' or '54' or '55') and len(str(card)) == 16:
		return 'Master'
	# Invalid
	else:
		return 'Invalid'

print ccValid(6011364837263748) #--> Output: "Discover"
print ccValid(5318273647283745) # --> Output: "Master" 
print ccValid(12345678910) # --> Output: "Invalid"  
print ccValid(371236473823677) # --> Output: "AMEX" 
print ccValid(4128374839283) # --> Output: "VISA"

'''
def credit(num):
    first_k = lambda k: int(str(num)[:k])
    l = len(str(num))
    is_discover = lambda: l == 16 and first_k(4) == 6011
    is_amex = lambda: l == 15 and first_k(2) in [34, 37]
    is_master = lambda: l == 16 and first_k(2) in range(51, 56)
    is_visa = lambda: l in [13, 16] and first_k(1) == 4
    checks = [
        (is_discover, "Discover"),
        (is_amex, "AMEX"),
        (is_master, "Master"),
        (is_visa, "VISA")
    ]
    for check, name in checks:
        if check(): 
            return name
    return "Invalid"

def credit(num):
    if str(num).startswith("6011") and len(str(num))==16: return "Discover"
    elif str(num).startswith("34") or str(num).startswith("37") and len(str(num))==15: return "AMEX"
    elif 51<=int(str(num)[:2])<=55 and len(str(num))==16: return "Master"
    elif str(num).startswith("4") and (len(str(num))==13 or len(str(num))==16): return "VISA"
    else: return "Invalid"
'''