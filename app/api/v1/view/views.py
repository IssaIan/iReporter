from flask_restful import Resource, reqparse
from flask import request
from app.api.v1.model.models import Models

    
parser = reqparse.RequestParser()
parser.add_argument(
    "title", type= str, required = True, help= "Title field is required"
    ""
)

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
        
    def patch(self, incident_id):
        data = request.get_json()
        incident = self.db.find(incident_id)
        if incident:
            incident.update(data)
            return {'Message' : 'Successfully updated',
                    'data' : incident
                    }, 200
        else:
            return self.notFound()
            
    def delete(self, incident_id):
        self.db.erase(incident_id)
        if True:
            return {'message' : 'Successful deletion'}, 200

class Incidents(Resource):
    def __init__(self):
        self.db = Models()
    
    def get(self):
        return {
            'Message' : 'Incidents returned successfully',
            'data' : self.db.all()
        }, 200

    def post(self):
        
        data = request.get_json()

        incident = {
            'type': data['type'],
            'title' : data['title'],
            'description' : data['description'],
            'images' : []
            }
        self.db.save(incident)
        return {'Message' : 'Incident saved successfully',
                'data' : incident
            }, 201
