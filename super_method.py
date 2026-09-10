class Student:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    @staticmethod
    def promot():
        print("The student has passed...")
    @staticmethod
    def fail():
        print("The student has failed...")
class PromotStudent():
    def __init__(self, name , type):
        self.name = name
        super().__init__(type)
s1 = Student("Jawad", "Regular")
print(s1.name)
print(s1.type)
s1.promot()

s2 = Student("Karim", "Irregular")
print(s2.name, s2.type)
s2.fail()