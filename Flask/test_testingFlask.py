from flask import json
import testingFlask as server
import unittest

class FlaskServerTest(unittest.TestCase):

	def setUp(self):
		# run app in testing mode to retrieve exceptions and stack traces
		server.app.testing = True
		self.app = server.app.test_client()

	def test_hello(self):
		response = self.app.get('/hello')
		# Checking for 200 OK status code 
		assert response.status_code == 200, "Status code was not OK"
		# --*-- assert on line 15 can also be written as the line below --*-- 
		# self.assertEqual(response.status_code, 200)

		# Check response data for content
		assert response.data == "Hello there!\n"

	def test_pets_get(self):
		response = self.app.get('/pets')
		# Checking for 200 OK status code 
		assert response.status_code == 200, "Status code was not OK"
		# Check response data for content
		assert response.data == "[]"


	# def test_pets_post(self):
	# 	response = self.app.post('/pets', data=json.dumps({
 #            'name': 'Jah',
 #            'age': '15',
 #            'species': 'human'
 #        }), content_type='application/json')
 #        # Checking for 200 OK status code 
	# 	assert response.status_code == 200, "Status code was not OK"
	# 	# Check response data for content
	# 	assert response.data == ''

	# def test_pets_name_get(self):

	# def test_pets_name_put(self):

	# def test_pets_name_delete(self):

		


# if this is run through the terminal, proceed
if __name__ == '__main__':
	unittest.main()