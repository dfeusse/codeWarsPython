'''
Temp Tracker: Max, Min, Mean and Mode

You've started a heating company with an oddly-mathematical All-Time Max, Min, Mean and Mode 
Temperature Guarantee.

Write a class TempTracker with these methods:

insert()    # records a new temperature
get_max()   # returns the highest temp we've seen so far
get_min()   # returns the lowest temp we've seen so far
get_mean()  # returns the mean of all temps we've seen so far
get_mode()  # returns the temp we've seen the most times so far
Do not store every single temperature inserted. You expect to get so much input that you won't 
be able to store all the temperatures in memory. Optimize for space and time. The time and space 
costs of your functions should all be O(1)!

The function to get the mean should return a float, but the rest of the get functions can return 
integers. If no temperatures have been inserted yet, the get functions should return null objects. 
Temperatures will all be inserted as integers. You'll record your temperatures in Fahrenheit, 
so you can assume they'll all be in the range 0 to 110.

If there is more than one mode, return any of the modes.

Note: this challenge was contributed by Interview Cake. If you get stuck, 
check it out for hints and gotchas that guide you to the solution by prompting you to 
have your own insights.
'''
class TempTracker():
	"""docstring for TempTracker"""
	def __init__(self, allTemps):
		#super(TempTracker, self).__init__()
		self.AllTemps = []
		#self.allTemps = []

	def insert(self, newTemp):
	#def insert(self):
		print 'inserting new temp'
		self.AllTemps.append(newTemp)
		return self.AllTemps

pone = TempTracker(1)
print pone.insert(5)
		