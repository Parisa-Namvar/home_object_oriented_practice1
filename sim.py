class Sim:
    def __init__(self, number, operator, owner, city=None):
        self.number = number
        self.operator = operator
        self.owner = owner
        self.city = city


    def save(self):
        print("SIM saved")
