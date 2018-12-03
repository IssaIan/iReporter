import unittest
import json
from app import create_app
from app.api.v1.model.models import users


app = create_app('testing')

class TestUsers(unittest.TestCase):

	def setUp(self):

		app.testing = True
		self.app = app.test_client()
		self.new_test_user = {
                'firstname' : 'Issa',
                'lastname' : 'Mwangi',
                'othernames' : 'Maina',
                'email' : 'issamwangi@gmail.com',
                'phoneNumber' : '0799170670',
                'username' : 'theonly', 
                'registered' : '11/28/2018'
                }

	def tearDown(self):
		users.clear()

	def test_create_user(self):
		response = self.app.post('/api/v1/users', 
												data = json.dumps(self.new_test_user), 
												headers={'content-type' : 'application/json'})
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'User saved successfully')
		self.assertEqual(response.status_code, 201)

	def test_fetch_user_byId(self):
		self.app.post('/api/v1/users', 
									data =json.dumps(self.new_test_user), 
									headers={'content-type' : 'application/json'})
		response = self.app.get('/api/v1/users/1')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'The specific user has been returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_fetch_all_users(self):
		response = self.app.get('/api/v1/users')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Users returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_user_update(self):
		self.app.post('/api/v1/users', 
									json = self.new_test_user,
									headers={'content-type' : 'application/json'})
		response = self.app.patch('/api/v1/users/1', json =  {
															'firstname' : 'Issa',
															'lastname' : 'Mwangi',
															'othernames' : 'Maina',
															'email' : 'issamwangi@gmail.com',
															'phoneNumber' : '0712345678',
															'username' : 'theonly', 
															'registered' : '11/28/2018'
															})
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()


