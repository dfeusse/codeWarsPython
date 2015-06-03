def capitals(word):
	#print [ i for i in word ]
	print [l for l in word if l.isupper()]
	index = -1
	listIndexes = []
	for i in word:
		index += 1
		if i.isupper():
			listIndexes.append(index)
	return listIndexes


print capitals('CodEWaRs') #, [0,3,4,6]

'''
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]

def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers
'''