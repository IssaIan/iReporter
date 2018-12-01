import unittest
import json
from app import create_app



app = create_app('testing')

class TestIncidents(unittest.TestCase):
	
	def setUp(self):
		
		app.testing = True
		self.app = app.test_client()
		self.new_test_incident = {
					'type' : 'red flag',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'images' : [],
					'videos' : []
					}
		
	def test_create_record(self):
		response = self.app.post('/api/v1/incidents', data = json.dumps(self.new_test_incident), headers={'content-type' : 'application/json'})
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incident saved successfully')
		self.assertEqual(response.status_code, 201)
	
	def test_get_incident_byId(self):
		response = self.app.get('api/v1/incidents/1')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'The specific incident has been returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_fetch_all_incidents(self):	
		response = self.app.get('/api/v1/incidents')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incidents returned successfully')
		self.assertEqual(response.status_code, 200)

	# def test_delete_incident(self):
	# 	response = self.app.delete('/api/v1/incidents/1')
	# 	result = json.loads(response.data)
	# 	self.assertEqual(result['message'], 'Successful deletion')
	# 	self.assertEqual(response.status_code, 200)

	# def test_update_incident(self):
	# 	self.app.post('/api/v1/incidents', data=json.dumps(self.new_test_incident), content_type='application/json')
	# 	self.app.post('/api/v1/incidents', data=json.dumps(self.new_test_incident), content_type='application/json')
	# 	response = self.app.patch(('/api/v1/incidents/1'))
	# 	result = json.loads(response.data)
	# 	self.assertEqual(result['Message'], 'Successfully updated')
	# 	self.assertEqual(result.status_code, 201)





if __name__ == '__main__':
	unittest.main()