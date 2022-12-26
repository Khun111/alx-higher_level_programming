#!/usr/bin/python3
'''Module to print square of size size'''
def print_square(size):
	'''Function to  print square of size size'''
	if not isinstance(size, int):
		raise TypeError('size must be an integer')
	if size < 0:
	    raise ValueError('size must be >= 0')
	for i in range(size):
		print('#' * size)
