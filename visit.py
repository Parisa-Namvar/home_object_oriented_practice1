class Visit:
    def __init__(self, city, doctor_name, specialist, price, visit_date):
        self.city = city
        self.doctor = doctor_name
        self.specialist = specialist
        self.price = price
        self.visit_date = visit_date
        self.visit_time = None

    def save(self):
        print("Visit saved")
