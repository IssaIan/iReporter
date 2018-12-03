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
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
		self.new_test_incident2 = {
					'type' : 'intervention',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
		self.new_test_incident3 = {
					'type' : 'intervention',
					'title' : 'yours',
					'status' : 'draft',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
		
		
	def test_create_record(self):
		response = self.app.post('/api/v1/incidents', 
									data = json.dumps(self.new_test_incident),
								 	headers={'content-type' : 'application/json'})
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incident saved successfully')
		self.assertEqual(response.status_code, 201)
	
	def test_get_incident_byId(self):
		response = self.app.get('/api/v1/incidents/1')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'The specific incident has been returned successfully')
		self.assertEqual(response.status_code, 200)

	def test_fail_getbyId(self):
		response = self.app.get('/api/v1/incidents/100')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Record not found')
		self.assertEqual(response.status_code, 404)

	def test_fetch_all_incidents(self):	
		response = self.app.get('/api/v1/incidents')
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incidents returned successfully')
		self.assertEqual(response.status_code, 200)


class TestUpdateIncidents(unittest.TestCase):

	def setUp(self):
		
		app.testing = True
		self.app = app.test_client()
		self.new_test_incident = {
					'type' : 'red flag',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
		self.new_test_incident2 = {
					'type' : 'intervention',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
		self.new_test_incident3 = {
					'type' : 'intervention',
					'title' : 'yours',
					'status' : 'draft',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}

	def test_update_incident_location(self):
		self.app.post('/api/v1/incidents', json = self.new_test_incident2)
		response = self.app.patch('/api/v1/incidents/1/location', 
									json ={ 
					'type' : 'intervention',
					'title' : 'yours',
					'status' : 'draft',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'karatina',
					'images' : [],
					'videos' : []}
					)							
		self.assertEqual(response.status_code, 200)

	def test_update_incident_description(self):
		self.app.post('/api/v1/incidents', json = self.new_test_incident3)
		response = self.app.patch('/api/v1/incidents/1/description', json =  {
					'type' : 'intervention',
					'title' : 'yours',
					'status' : 'draft',
					'description' : 'this is the new description',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					})
		self.assertEqual(response.status_code, 200)

	def test_updating_a_nonexistence_incident(self):
		self.app.post('/api/v1/incidents', json = self.new_test_incident2)
		response = self.app.patch('/api/v1/incidents/20/description', json =  {
					'type' : 'intervention',
					'title' : 'yours',
					'status' : 'draft',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					})
		self.assertEqual({'Message' : 'Record not found', 'status': 404 }, response.get_json())
		
	
	
class TestdeleteIncident(unittest.TestCase):
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
		self.new_test_incident2 = {
					'type' : 'intervention',
					'title' : 'mine',
					'status' : 'Under-investigation',
					'description' : 'Collection of bribes in the KRA building',
					'location' : 'Nyeri',
					'images' : [],
					'videos' : []
					}
	def test_create_record(self):
		response = self.app.post('/api/v1/incidents', data = json.dumps(self.new_test_incident2), headers={'content-type' : 'application/json'})
		result = json.loads(response.data)
		self.assertEqual(result['Message'], 'Incident saved successfully')
		self.assertEqual(response.status_code, 201)

	def test_delete_incident(self):
		self.app.post('/api/v1/incidents', json = self.new_test_incident)
		response = self.app.delete('/api/v1/incidents/1')
		self.assertEqual({'Message' : 'Successful deletion'}, response.get_json())
		self.assertEqual(response.status_code, 200)

	def test_fail_delete_incident(self):
		self.app.post('/api/v1/incidents', json = self.new_test_incident)
		response = self.app.delete('/api/v1/incidents/200')
		self.assertEqual({'Message' : 'Record not found', 'status': 404 }, response.get_json())
		


if __name__ == '__main__':
	unittest.main()