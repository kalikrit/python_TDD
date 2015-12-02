from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	"""
	Tests are organised into classes, 
	which inherit from unittest.TestCase.
	"""

	"""
	setUp and tearDown are special methods which get run before and after each test. 
	I’m using them to start and stop our browser—note that they’re a bit like a try/except, 
	in that tearDown will run even if there’s an error during the test itself
	No more Firefox windows left lying around! 
	"""
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		"""
		The main body of the test is in a method called test_can_start_a_list_and_re trieve_it_later. 
		Any method whose name starts with test_ is a test method, and will be run by the test runner. 
		You can have more than one test_ method per class. 
		Nice descriptive names for our test methods are a good idea too. 
		"""
		self.browser.get('http://localhost:8000')
		"""
		We use self.assertIn instead of just assert to make our test assertions. 
		unittest provides lots of helper functions like this to make test assertions, 
		like assertEqual, assertTrue, assertFalse, and so on. 
		You can find more in the unittest documentation (https://docs.python.org/3/library/unittest.html) 
		"""
		self.assertIn('To-Do', self.browser.title)
		"""
		self.fail just fails no matter what, producing the error message given. 
		I’m using it as a reminder to finish the test. 
		"""
		self.fail('Finish the test!')

if __name__ == '__main__':

	unittest.main(warnings='ignore')