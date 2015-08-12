'''
def up_array(numList):
	for i in numList:
		if i < 0 or i > 10:
			return None
    num = int(''.join(map(str, numList))) + 1
    print num
    return map(int, str(num))
'''
def up_array(numList):
    for i in numList:
    	if i < 0 or i > 10:
    		return None
    return map(int, str(int(''.join(map(str, numList))) + 1))
   
print(up_array([2,3,9]))#, [2,4,0])
print(up_array([4,3,2,5]))#, [4,3,2,6])
print(up_array([1,-9]))#, None)