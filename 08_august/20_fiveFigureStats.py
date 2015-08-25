'''
Background

A simple statistical analysis of a series of samples can be done with a Five Figure Summary.

The five figure summary gives the lower extreme, upper extreme, lower quartile, 
median, and upper quartile derived from the supplied sample data.

Confusingly, the five figure summary often includes a sixth value, which is the 
number of samples in the series.

In this Kata you will be given a class outline to complete. The class will be 
instantiated with a sequence of values, and you must implement the method to 
return the six-figure version of a five figure summary.

You are expected to do thre calculations yourself, using pandas or numpy will get you a 
squinty frown from your sensei! :)

Inputs

At class instantiation you will be given a sequence of values. This sequence may contain 
non-numerical values, these should be ignored.
At summary creation you will be given a maximum precision for numerical results. 
In None is supplied, assume full precision is to be returned.

Calculations

N: Number of valid numeric values in the sequence.
Lower Extreme: The smallest value contained within the sequence.
Upper Extreme: The largest value contained within the sequence.
Median: The centre value of the sorted sequence of valid values.
Lower Quartile: The boundary value between the first and second quarters of the sorted 
sequence of valid values.
Upper Quartile: The boundary value between the third and fourth quarters of the sorted 
sequence of valid values.
The median and both quartiles may need to be a linear interpolation between two values.

Linear Interpolation Examples

Given a sequence of values [2, 3, 4, 5, 6, 7, 8, 9]

Position 3.5 would return the mid-point between the values at index 3 and index 4 returning 5.5.
Position 1.25 would return the quarter-point between the values at index 1 and index 2 returning 3.25.
Position 6.75 would return the three-quarter-point between the values at index 6 
and index 7 returning 7.75.
Outputs

You will return a tuple with the calculated values in the following order:

(N, lower_extreme, upper_extreme, lower_quartile, median, upper_quartile)
Where no precision is defined, and given the rouding/quantization errors with floating 
point processing, your answers must be within 10 ** -10 of the correct answer. 
Where precision is defined, your answer is expected to be exact.

Worked Example

data = range(0, 7)
StatisticalSummary(data).five_figure_summary(2) # => (7, 0, 6, 1.5, 3, 4.5)
'''

# import pandas # I'm watching you!
# import numpy  # Don't do it!

class StatisticalSummary(object):
    def __init__(self, seq):
        self.seq = seq

	def N():
'''
	def lower_extreme():
	def upper_extreme():
	def median():
	def lower_quartile():
	def upper_quartile():
'''
    def five_figure_summary(self, precision=None):
        #return ("N", "extreme_lower", "extreme_upper", "lower_quartile", "median", "upper_quartile")
        #return (tuple of above results)

#data = range(0, 7)
#StatisticalSummary(data).five_figure_summary(2) # => (7, 0, 6, 1.5, 3, 4.5)