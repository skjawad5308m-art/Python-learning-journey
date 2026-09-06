class Student:
    University_name = "MIT"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def welcome(self):
        print("welcome student," ,self.name)

    def get_age(self):
        return self.age

s1 = Student("Jawad", 19)
s1.welcome()
print(s1.get_age())