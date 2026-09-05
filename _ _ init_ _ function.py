class Student:
    def __init__(self, fullname, grade, year):
        self.name = fullname
        self.grade = grade
        self.year = year
s1 = Student("full name: MD.Sujnain Jawad", "Grade: GPA 5.00", "year:  2026" )
print(s1.name)
print(s1.grade)
print(s1.year)

s2 = Student("Bipro Borno Sutar", "GPA 4.78", "2026")
print(s2.name)
print(s2.grade)
print(s2.year)

class Universities:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking = ranking
u1 = Universities("MIT", "1")
print(u1.name)
print(u1.ranking)

u2 = Universities("Harvard", "8")
print(u2.name)
print(u2.ranking)

class Countries:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose
c1 = Countries("United States of America", "Study")
print(c1.name)
print(c1.purpose)

c2 = Countries("Europe", "Research and Job")
print(c2.name)
print(c2.purpose)