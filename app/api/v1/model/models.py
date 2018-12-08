
class Models():
    """ This class contains functions that allow requests on both incidents and users """

    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items

    def save(self, data):
        data['id'] = self.__generate_id()
        self.items.append(data)

    def find(self, id):
        for item in self.items:
            if item['id'] == id:
                return item

    def erase(self, id):
        item = self.find(id)
        if not item:
            return None
        else:
            self.items.remove(item)
            return item

    def __generate_id(self):
        if len(self.items):
            return self.items[-1]['id'] + 1
        else:
            return 1

    def find_by_username(self, itemname):
        for item in self.items:
            if item['username'] == itemname:
                return item
