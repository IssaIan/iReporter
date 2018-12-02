from flask_restful import Resource, reqparse
from flask import request
from app.api.v1.model.models import Models

    
# parser = reqparse.RequestParser()
# parser.add_argument(
#     "type", type= str, required = True, help= "Type field is required")
# parser.add_argument(
#     "title", type= str, required = True, help= "Title field is required")
# parser.add_argument(
#     "description", type= str, required = True, help= "Description field is required")
# args = parser.parse_args()


class Incident(Resource):
    def __init__(self):
        self.db = Models()
        
    def notFound(self):
        return {'Message' : 'Record not found','status':404},404

    def get(self, incident_id):
        incident = self.db.find(incident_id) 
        if not incident:
            return self.notFound()    
        else:
            return {'Message' : 'The specific incident has been returned successfully',
                    'data' : incident
                    }, 200
            
    def delete(self, incident_id):
        incident = self.db.erase(incident_id)
        if not incident:
            return self.notFound()     
        else:
            return {'Message' : 'Successful deletion'}, 200           


class Incidents(Resource):
    def __init__(self):
        self.db = Models()
    
    def notFound(self):
        return {'Message' : 'No records found','status':404},404
    
    def get(self):
        if self.db.all() == []:
            return self.notFound() 
        return {
                'Message' : 'Incidents returned successfully',
                'data' : self.db.all()
                }, 200

    def post(self):
        
        data = request.get_json()

        incident = {
            'type': data['type'],
            'title' : data['title'],
            'status': data['status'],
            'description' : data['description'],
            'images' : [],
            'videos' : []
            }
        self.db.save(incident)
        return {'Message' : 'Incident saved successfully',
                'data' : incident
            }, 201

class Location(Resource):
    def __init__(self):
        self.db = Models()

    
    def notFound(self):
        return {'Message' : 'Record not found','status':404},404
    
    def patch(self, incident_id):
        data = request.get_json()
        incident = self.db.find(incident_id)
        if incident:
            for incident['location'] in incident:
                incident.update(data)
                return {'Message' : 'Successfully updated',
                    'data' : incident
                    }, 200
        else:
            return self.notFound()
       


class Description(Resource):
    def __init__(self):
        self.db = Models()

    
    def notFound(self):
        return {'Message' : 'Record not found','status':404},404
    
    def patch(self, incident_id):
        data = request.get_json()
        incident = self.db.find(incident_id)
        if incident:
            for incident['description'] in incident:
                incident.update(data)
                return {'Message' : 'Successfully updated',
                    'data' : incident
                    }, 200
        else:
            return self.notFound()