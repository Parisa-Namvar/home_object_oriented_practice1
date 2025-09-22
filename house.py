class House:
    def __init__(self, city, price, area, address = None):
        self.city = city
        self.price = price
        self.area = area
        self.address = address

    def save(self):
        print("House saved")
