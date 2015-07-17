'''
1) the first and last characters remain in original place for each word
2) characters between the first and last characters must be sorted alphabetically
3) punctuation should remain at the same place as it started, for example: shan't -> sahn't

Assumptions
1) words are seperated by single spaces
2) only spaces separate words, special characters do not, for example: tik-tak -> tai-ktk
3) for this kata puctuation is limited to 4 characters: hyphen(-), apostrophe('), comma(,) and period(.) 
4) ignore capitalisation
'''
import re

def typoglycemia(string):
	print string.split(' ')
	for w in string.split(' '):
		#word = re.split(r"\s+|[,'.-]\s*", w)
		word = re.split('(\W)', w)
		print word



print typoglycemia("hey tik.tak you")
#print typoglycemia
# print typoglycemia