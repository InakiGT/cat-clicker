
class Cat:
    def __init__(self, id, name, img, count=0):
        self.id = id
        self.name = name
        self.img = img
        self.count = count
        
    def add_count(self):
        self.count += 1