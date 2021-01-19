class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    def cumlaude_check(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False