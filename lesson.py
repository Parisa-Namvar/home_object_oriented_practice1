class Course:
    def __init__(self, course, prof, credit, start=None):
        self.course = course
        self.prof = prof
        self.credit = credit
        self.start = start

    def save(self):
        print("Course saved")
