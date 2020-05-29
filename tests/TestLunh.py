from model.Lunh import Lunh
import unittest

class TestLunh(unittest.TestCase):

	def setUp(self):
		self.lunh = Lunh()

	def tearDown(self):
		self.lunh = None

	def test_zero(self):
		self.assertFalse(self.lunh.checksum(0), "Zero number accepted")

	def test_negative_number(self):
		self.assertFalse(self.lunh.checksum(-1), "Negative number accepted")

	def test_valid_number(self):
		self.assertTrue(self.lunh.checksum(4751280029911063), "Valid number rejected")

	def test_invalid_number(self):
		self.assertFalse(self.lunh.checksum(4751280029911073), "Invalid number accepted")

if __name__ == '__main__':
    unittest.main()
