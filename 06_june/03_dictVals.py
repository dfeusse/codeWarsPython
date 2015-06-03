'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas 
except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa &amp; Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart &amp; Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''
def namelist(names):
	vals = [ i['name'] for i in names ]
	if len(vals) > 2:
		firstPt = vals[:len(vals)-2]
		lastPt = vals[-2:]
		return ', '.join(firstPt) + ', ' + ' &amp; '.join(lastPt)
	elif len(vals) == 2:
		return ' &amp; '.join(vals)
	else:
		return ''.join(vals)


print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa &amp; Maggie'

print namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart &amp; Lisa'

print namelist([ {'name': 'Bart'} ])
# returns 'Bart'

print namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Dan'} ])
# returns 'Bart, Lisa &amp; Maggie'

'''
def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''

'''