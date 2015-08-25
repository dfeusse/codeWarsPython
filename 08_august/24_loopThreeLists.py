lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]

for a, b, c in itertools.izip(lst1, lst2, lst3):
	print a,b,c

# ---------------------------

pone = []

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]
for a, b, c in itertools.izip(lst1, lst2, lst3):
	emma = {}
	emma['name'] = a
	emma['price'] = b
	emma['img'] = c
	pone.append(emma)

print pone