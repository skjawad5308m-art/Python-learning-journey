class Person:
    def __init__(self, name,age, city ):
        self.__name = name
        self.age = age
        self.city = city
    def __welcome(self):
        print("Welcome Jawad")
p1 = Person("Jawad", "17", "Dhaka")
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.__welcome())

# for using underscore before name and welcome these has become private . I cannot be seen in the output anymore

