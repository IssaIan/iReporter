import unittest
import json
from app import create_app
from app.api.v1.model.models import users

class TestUsers(unittest.TestCase):
	def setUp(self):
		self.app = create_app()
		self.app.testing = True
		self.client = self.app.test_client()

	def create_user(self):

		new_test_user = {
                'firstname' : 'Issa',
                'lastname' : 'Mwangi',
                'othernames' : 'Maina',
                'email' : 'issamwangi@gmail.com',
                'phoneNumber' : '0799170670',
                'username' : 'theonly', 
                'registered' : '11/28/2018',
                }
		response = self.client.post('/api/v1/users',
					data = json.dumps(new_test_user),
					headers = {"content-type" : "application/json"})
		return response

	def test_create_user(self):
		user = self.create_user()
		result = json.loads(user.data)
		self.assertEqual(result['Message'], 'User saved successfully')
		self.assertEqual(user.status_code, 201)

	def test_fetch_user(self):
		self.create_user
		result = self.app.get('/api/v1/users')
		self.assertEqual(result['Message'], 'Users returned successfully')
		self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
	unittest.main()


