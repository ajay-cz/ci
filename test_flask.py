import math
import unittest
import requests



r = requests.get('http://0.0.0.0:5000/')


class SimpleFlaskTest(unittest.TestCase):
	response = r.text
	flag = False
	def test_flask(self):
		print(self.__class__.response)
		self.assertTrue(self.__class__.flag,msg="the api json response it not fine")
