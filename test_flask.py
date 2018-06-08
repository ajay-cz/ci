import math
import unittest



class SimpleFlaskTest(unittest.TestCase):
  flag = False
  def test_flask(self):
		self.assertTrue(flag,msg="the api json response it not fine")
