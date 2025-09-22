class Person:
    def __init__(self, name, family, national_id, city = None):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.city = city

    def save(self):
        print("Person saved")
