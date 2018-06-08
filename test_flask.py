import math
import unittest
from urllib.request import Request, urlopen



class SimpleFlaskTest(unittest.TestCase):
	req = Request("http://0.0.0.0:5000/")
	response = urlopen(req)
	flag = False
	def test_flask(self):
		print(self.__class__.response)
		self.assertTrue(self.__class__.flag,msg="the api json response it not fine")
