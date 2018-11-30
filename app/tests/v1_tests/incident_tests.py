import unittest
import json
from app import create_app


app = create_app()

class TestIncidents(unittest.TestCase):
	
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True
	
	def create_record(self):
		new_test_incident = {
					'type' : 'red flag',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'images' : [],
					'videos' : []
					}
		response = self.app.post('/api/v1/incidents', data=json.dumps(new_test_incident), content_type='application/json')
		return response

	def test_create_record(self):
		incident = self.create_record()
		result = json.loads(incident.data)
		self.assertEqual(result['Message'], 'Incident saved successfully')
		self.assertEqual(incident.status_code, 201)
	
	def test_fetch_incident_byId(self):
		new_test_incident = {
					'type' : 'red flag',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'images' : [],
					'videos' : []
					}
		response = self.app.post('/api/v1/incidents/1', data=json.dumps(new_test_incident), content_type='application/json')
		return response
		result = self.app.get('/api/v1/incidents/1')
		failed_result = self.app.get('/api/v1/incidents/12334')
		
		self.assertEqual(result.get_json(), {'Message' : 'The specific incident has been returned'})
		self.assertEqual(result.status_code, 200)
		self.assertEqual(failed_result.get_json(), {'Message' : 'Record not found'})
		self.assertEqual(failed_result.status_code, 404)

	def test_fetch_incidents(self):
		self.create_record()
		
		response = self.app.get('/api/v1/incidents')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incidents returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_delete_incident(self):
		response = self.app.delete('/api/v1/incidents/1')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Successful deletion')
		self.assertEqual(response.status_code, 200)

	def test_update_incident(self):
		new_test_incident = {
					'type' : 'red flag',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'images' : [],
					'videos' : []
					}
		response = self.app.post('/api/v1/incidents', data=json.dumps(new_test_incident), content_type='application/json')
		return response
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Successfully updated')
		self.assertEqual(result.status_code, 201)





if __name__ == '__main__':
	unittest.main()