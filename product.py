class Product:
    def __init__(self, name, price, brand, generate_date):
        self.name = name
        self.price = price
        self.brand = brand
        self.generate_date = generate_date
        self.expiration_date = None

    def save(self):
        print("Product saved")
