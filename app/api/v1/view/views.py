from flask_restful import Resource, reqparse
from flask import request
from app.api.v1.model.models import Models

    
parser = reqparse.RequestParser()
parser.add_argument(
    "type", type= str, required = True, help= "Type field is required")
parser.add_argument(
    "title", type= str, required = True, help= "Title field is required")
parser.add_argument(
    "status", type=str, default= "Draft"
)
parser.add_argument(
    "description", type= str, required = True, help= "Description field is required"
    )
parser.add_argument(
    "location", type= str, required = True, help= "Location field is required")
parser.add_argument(
    "images", type= str, required = False)
parser.add_argument(
    "videos", type= str, required = False)


class GetError():
    #declare a function notFound() to enble inheritance of the function by other classes

    def notFound(self):
        return {'Message' : 'Record not found','status':404},404
    

class Incident(Resource, GetError):
    #This class and its members creates an endpoint where only a single incident can be acted upon

    def __init__(self):
        self.db = Models()

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


class Incidents(Resource, GetError):
    #This class and its members creates an endpoint where only several incidents can be acted upon

    def __init__(self):
        self.db = Models()
   
    def get(self):
        if self.db.all() == []:
            return self.notFound() 
        return {
                'Message' : 'Incidents returned successfully',
                'data' : self.db.all()
                }, 200

    def post(self):
        
        data = parser.parse_args()

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

class Location(Resource, GetError):
    #This class and its members creates an endpoint where only a single incident's location can be updated 

    def __init__(self):
        self.db = Models()
    
    def patch(self, incident_id):

        data = parser.parse_args()

        incident = self.db.find(incident_id)
        if incident:
            for incident['location'] in incident:
                incident.update(data)
                return {'Message' : 'Successfully updated',
                    'data' : incident
                    }, 200
        else:
            return self.notFound()
       


class Description(Resource, GetError):
    #This class and its members creates an endpoint where only a single incident's descriptionp can be updated 

    def __init__(self):
        self.db = Models()
   
    def patch(self, incident_id):

        data = parser.parse_args()

        incident = self.db.find(incident_id)
        if incident:
            for incident['description'] in incident:
                incident.update(data)
                return {'Message' : 'Successfully updated',
                    'data' : incident
                    }, 200
        else:
            return self.notFound()