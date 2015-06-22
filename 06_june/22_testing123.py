'''
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

Examples

number([]) # =&gt; []
number(["a", "b", "c"]) # =&gt; ["1: a", "2: b", "3: c"]
'''
def number(strings):
	length = range(1,len(strings)+1)
	return [ str(a) + ": " + b for a, b in zip(length, strings)]


print number([]) # =&gt; []
print number(["a", "b", "c"]) # =&gt; ["1: a", "2: b", "3: c"]

'''
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

def number(lines):
    return ["{0}: {1}".format(i + 1, lines[i]) for i in xrange(len(lines))]

def number(lines):
    return ['{}: {}'.format(n, s) for (n, s) in enumerate(lines, 1)]
'''