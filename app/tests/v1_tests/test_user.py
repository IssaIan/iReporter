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
				'password' : 'Maina9176',
                'phoneNumber' : '0799170670',
                'username' : 'theonly', 
                'registered' : '11/28/2018'
                }
		self.new_test_user2 = {
				'firstname' : 'Ian',
                'lastname' : 'Mwangi',
                'othernames' : 'Maina',
                'email' : 'issa2mwangi@gmail.com',
				'password' : 'Maina9176',
                'phoneNumber' : '0769170670',
                'username' : 'only', 
                'registered' : '11/28/2018'
		}
		self.new_test_user3 = {
				'firstname' : 'Julie',
                'lastname' : 'Mwangi',
                'othernames' : 'Maina',
                'email' : 'juliemwangi@gmail.com',
				'password' : 'Maina9176',
                'phoneNumber' : '0779170670',
                'username' : 'julietheonly', 
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
									data =json.dumps(self.new_test_user2), 
									headers={'content-type' : 'application/json'})
		response = self.app.get('/api/v1/users/1')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'The specific user has been returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_fetch_user_byUsername(self):
		self.app.post('/api/v1/users/', 
									data =json.dumps(self.new_test_user3), 
									headers={'content-type' : 'application/json'})
		response = self.app.get('/api/v1/users/julietheonly')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'The specific user has been found')
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
															'password' : 'Iamok',
															'phoneNumber' : '0712345678',
															'username' : 'theonly', 
															'registered' : '11/28/2018'
															})
		self.assertEqual(response.status_code, 200)

	def test_user_update_by_username(self):
		self.app.post('/api/v1/users', 
									json = self.new_test_user,
									headers={'content-type' : 'application/json'})
		response = self.app.patch('/api/v1/users/theonly', json =  {
															'firstname' : 'Issa',
															'lastname' : 'Mwangi',
															'othernames' : 'Maina',
															'email' : 'issamwangi@gmail.com',
															'password' : 'Iamok',
															'phoneNumber' : '0712345678',
															'username' : 'theonly', 
															'registered' : '11/28/2018'
															})
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()


