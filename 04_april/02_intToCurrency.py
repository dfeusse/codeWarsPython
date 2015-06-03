'''
Write a function that takes an integer in input and outputs a string with currency format.

Integer in currency format is expressed by a string of number where every three characters are 
separated by comma.

Ex. 123456 -> "123,456"
'''

def to_currency(price):
	priceString = str(price)
	currency = ""
	index = 0
	strLen = len(priceString)
	for i in priceString:
		index = index + 1
		currency = currency + i
		if (strLen - index) % 3 == 0 and index != strLen:
			currency = currency + ","
	return currency

print to_currency(1234)
print to_currency(12345)
print to_currency(123456)
print to_currency(123456789)

'''
def to_currency(price):
    str_price = str(price)[::-1]
    return ','.join([str_price[i:i+3] for i in range(0, len(str_price), 3)])[::-1]

def to_currency(price):
    price=list(str(price))
    for i in range(3,len(price),3):
        price[-(i+i/3-1):-(i+i/3-1)]=','
    return "".join(price)
'''