'''
Caesar Ciphers are one of the most basic forms of encryption. It consists of a message and a key, 
and it shifts the letters of the message for the value of the key.

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns 
the encrypted message.

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. All punctuation, 
numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
'''
import string

def encription(message, key):
	if key > 26:
		newkey = key/26
	else:
		newkey = key
	newMessage = ''
	alphabet = string.ascii_lowercase
	for m in message:
		if m.isalpha() == True:
			if m.islower():
				newMessage = newMessage + alphabet[alphabet.index(m) + newkey] 
			else:
				alphabetUpper = string.ascii_uppercase
				newMessage = newMessage + alphabetUpper[alphabetUpper.index(m) + newkey] 
		else:
			newMessage = newMessage + m
	return newMessage

print encription('Caesar Cipher', 1)
print encription('Caesar Cipher', -1)
print encription('Caesar Cipher', 27)