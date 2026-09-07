class Student:
    def __init__(self):
        self.sub1 = 40
        self.sub2 = 33
        self. sub3 = 29
        print("The student has failed")
    def promot(self):
        self.sub1 = 88
        self.sub2 = 90
        self.sub3 = 76
        print("The student has passed now...")
s1 = Student()
s1.promot()

#abstraction hides unnecessary lines and shows the final output