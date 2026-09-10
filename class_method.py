class Person:
    name = "Jawad"
    def changeName(self, name):
        self.name = name
p1 = Person()
p1.changeName("MD.Sujnain Jawad.")
print(p1.name)
print(Person.name)
#Here the name of p1 has changed but person name is still unchanged

class Person:
    name = "Jawad"
    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("MD.Sujnain Jawad.")
print(p1.name)
print(Person.name)
#Here in these method bot has changed. There are other ways to do it as well

class Person:
    name = "Jawad"
    def changeName(self, name):
        self.__class__.name = name
p1 = Person()
p1.changeName("MD.Sujnain Jawad.")
print(p1.name)
print(Person.name)

class Person:
    name = "Jawad"
    @classmethod
    def changeNmae(cls, name):
        cls.name = name
p1 = Person()
p1.changeNmae("MD.Sujnain Jawad.")
print(p1.name)
print(Person.name)

#These all the ways through which we can change name of both person and p1