'''
You decide to test if your oddly-mathematical heating company is fulfilling its 
All-Time Max, Min, Mean and Mode Temperature Guarantee
Write a class TempTracker with these methods:

insert() - records new temp
get_max() - returns highest temp seen so far
get_min() - return slowest temp seen so far
get_mean() - returns mean of all temps seen so far
get_mode() - returns mode of all temps seens so far

Optimize for space and time. Favor speeding up the get_ functions over speeding up the 
insert() function.

get_mean() should return a float, but the rest of the get_ functions can return integers. 
Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, 
so we can assume they'll all be in the range 

If there is more than one mode, return any of the modes.
'''

'''
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
'''

class TempTracker():
		"""docstring for ClassName"""
		# need insert, get_max, get_min, get_mean, get_mode
		temperatures = []

		def __init__(self, temperature):
			self.temperature = temperature

		def show_temperature(self):
			print 'temperature is: ' + str(self.temperature)

		def get_temperatures(self):
			return 'list of temperatures are: ' + str(self.temperatures)


'''
class Parent():
	def __init__(self, last_name, eye_color):
		print 'Parent constructor called'
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print 'Last name: ' + self.last_name
		print 'Eye color: ' + self.eye_color
'''