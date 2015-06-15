from collections import Counter
def count(array):
    #your code here
    return Counter(array)

'''
from collections import Counter
def count(array):
    return Counter(array)

def count(array):
    result = {}
    for x in array:
        result[x] = result.get(x, 0) + 1
    return result
'''