class Person:
    def __init__(self, name, family, national_id, city = None, date_of_birth = None):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.city = city
        self.date_of_birth = date_of_birth

    def save(self):
        print("Person saved")
