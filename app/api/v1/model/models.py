incidents = []
users = []

class Models():
    def __init__(self):
        self.incidents = incidents
    
    def all(self):
        return self.incidents

    def save(self, data):
        data['id'] = self.__generate_id()
        self.incidents.append(data)

    def find(self, id):
        for incident in self.incidents:
            if incident.values()[-1] == id:
                return incident
           
        
    def erase(self, id):
        incident = self.find(id)
        self.incidents.remove(incident)
        return True

    def __generate_id(self):
        if len(self.incidents):
            return self.incidents[-1]['id'] + 1
        else:
            return 1

class UserModels():
    def __init__(self):
          self.users = users

    def all(self):
        return self.users

    def save(self, data):
        data['id'] = self.__generate_id()
        self.users.append(data) 
    
    def find(self, id):
        for user in self.users:
            if user.values()[-1] == id:
                return user
            else:
                return None
    def __generate_id(self):
        if len(self.users):
            return self.users[-1]['id'] + 1
        else:
            return 1

    