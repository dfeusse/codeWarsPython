'''
According to wiki palindrome is a word, phrase, number, or other sequence of characters which 
reads the same backward or forward. Allowances may be made for adjustments to capital letters, 
punctuation, and word dividers. 
Famous examples include "A man, a plan, a canal, Panama!", "Amor, Roma", "race car" 
and "No 'x' in Nixon".

All requirements from definition should be fulfilled. In case of null input (None for Python) 
return false.
'''
import string

def palindrome(s):
	return "".join(l for l in s if l not in string.punctuation).lower().replace(" ", "") == "".join(l for l in s if l not in string.punctuation).lower().replace(" ", "")[::-1] if s != None else False

print palindrome("A man, a plan, a canal, Panama!")

'''
def is_palindrome(s):
    if s is not None:
      wor=[wo.lower() for wo in s if wo.isalnum()]
      if wor==wor[::-1]:return True
        return False
    
    else:
      return False
'''