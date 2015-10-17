'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
'''
def validate_pin(string):
	#return True if len([ int(s) for s in string ]) == 4 or len([ int(s) for s in string ]) == 6 else False
	return True if len([ s for s in string ]) == 4 or len([ s for s in string ]) == 6 else False
	#print len([ s for s in string ])

'''
print validate_pin("1234")# == True
print validate_pin("12345")# == False

print(validate_pin("1"))#False)
print(validate_pin("1234567"))#False)

print(validate_pin("1111"))#True)
print(validate_pin("123456"))#True)
'''
print(validate_pin("-1234"))#False)
print(validate_pin(""))#False)