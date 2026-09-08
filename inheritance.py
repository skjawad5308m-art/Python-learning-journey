class Student:
    @staticmethod
    def promot():
        print("The student has passed...")
    @staticmethod
    def fail():
        print("The student has failed..")
    def __init__(self,name):
        self.name = name
s1 = Student("Jawad")
s1.promot()
s2 = Student("Ladip")
s2.fail()
