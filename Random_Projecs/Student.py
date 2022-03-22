

class Student:   #desines what a student is // templateS
    
    def __init__(self, name, major, gpa):
        self.name = name       #name = name passes in function
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

