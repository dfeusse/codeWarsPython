'''


Examples :

iq_test("2 4 7 8 10") == 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") == 2 // Second number is even, while the rest of the numbers are odd
'''

def iq_test(string):
	stringList = string.replace(" ",",").split(',')
	# outputs: ['2', '4', '7', '8', '10']
	if int(stringList[0]) % 2 == 0:
		evenOrOdd = 'even'
	else:
		evenOrOdd = 'odd'

	index = 0
	for i in stringList:
		index += 1
		if int(i) % 2 == 0:
			tempOddEven = 'even'
		else:
			tempOddEven = 'odd'
		if tempOddEven != evenOrOdd:
			return index

print(iq_test("2 4 7 8 10"))
print(iq_test("1 2 1 1"))