#/usr/bin/python3
'''Module for testing Rectangle Class'''
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
class Test_Rectangle(TestCase):
	'''Tests Class to test rectangle'''
	def test_rectangle_attr(self):
		r1 = Rectangle(10, 2)
		r2 = Rectangle(2, 10)
		r3 = Rectangle(10, 2, 0, 0, 12)
		self.assertEqual(r1.id, 1)
		self.assertEqual(r2.id, 2)
		self.assertEqual(r3.id, 12)
	def test_validation(self):
		r1 = Rectangle(10, '2')
		self.assertRaises(TypeError)
if __name__ == '__main__':
	unittest.main()
