'''
unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
Note:

Result string should be sorted
The test case won't pass Integer with leading zero
'''
def unused_digits(*arg):
	a = list(set( [ int(i) for i in sorted(''.join(str(i) for i in arg)) ] ))
	b = sorted(list(set(range(10))-set(a)))
	return ''.join(str(z) for z in b)

print unused_digits(12, 34, 56, 78) # "09"
print unused_digits(2015, 8, 26) # "3479"

'''
def unused_digits(*args):
    incoming = list(''.join(str(a) for a in args))
    digits = list('0123456789')
    while digits and incoming:
        cursor = incoming.pop()
        if cursor in digits:
            digits.remove(cursor)
    return ''.join(digits)
'''