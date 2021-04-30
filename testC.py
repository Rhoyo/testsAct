import unittest
import calc

class test(unittest.TestCase):
	

#testCases
	def test_A(self):
		result=calc.add(5,6)
		self.assertEqual(result, 11)

	def test_S(self):
		result=calc.sub(5,6)
		self.assertEqual(result, -1)

	def test_M(self):
		result=calc.mult(5,6)
		self.assertEqual(result, 30)

	def test_S(self):
		result=calc.div(8,4)
		self.assertEqual(result, 2)

