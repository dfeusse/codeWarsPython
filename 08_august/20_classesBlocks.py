'''
Write a class Block that creates a block (Duh..)

The constructor should take an array as an argument, this will contain 3 integers 
of the form [width, length, height] from which the Block should be created.

Define these methods:

`get_width()` return the width of the `Block`

`get_length()` return the length of the `Block`

`get_height()` return the height of the `Block`

`get_volume()` return the volume of the `Block`

`get_surface_area()` return the surface area of the `Block`
'''

class Block():
	"""docstring for Block"""
	def __init__(self, dimensions):
		#super(Block, self).__init__()
		self.dimensions = dimensions
		self.width = self.dimensions[0]
		self.length = self.dimensions[1]
		self.height = self.dimensions[2]

	def get_width(self):
		return self.width

	def get_length(self):
		return self.length

	def get_height(self):
		return self.height

	def get_volume(self):
		return self.width * self.length * self.height

	def get_surface_area(self):
		return (2 * (self.width * self.length)) + (2 * (self.width * self.height)) + (2 * (self.length * self.height))

b = Block([2,4,6]) # -> create a `Block` object with a width of `2` a length of `4` and a height of `6`
print b
print b.get_width() #-> return 2
print b.get_length() #-> return 4
print b.get_height()# -> return 6
print b.get_volume() #-> return 48
print b.get_surface_area()# -> return 88