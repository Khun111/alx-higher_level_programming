#!/usr/bin/python3
'''Module for Unit tests of Class Base'''
import os
import unittest
from models.base import Base
class Test_Base(unittest.TestCase):
	'''Test class for Base'''
	def test_base_id(self):
		b1 = Base()
		b2 = Base()
		b3 = Base()
		b4 = Base(12)
		b5 = Base(None)
		self.assertEqual(b1.id, b3.id - 2)
		self.assertEqual(b4.id, b5.id + 8)
		self.assertEqual(b5.id, 4)

if __name__ == "__main__":
    unittest.main()
