class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
s1 = Student(96, 92, 90)
print(s1.phy)
print(s1.chem)
print(s1.math)
print(s1.percentage)
s1.phy = 98
print(s1.phy)
print(s1. percentage)
#Here the number of physics has changed but the percentage is unchanged

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
s1 = Student(96, 92, 90)
print(s1.phy)
print(s1.chem)
print(s1.math)
print(s1.percentage)
s1.phy = 98
print(s1.phy)
s1.calcPercentage()
print(s1.percentage)
#By using these method we can change the percentage as well

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
@property
def percentage(self):
    return str((self.phy + self.chem + self.math) / 3) + "%"
p1 = Student(96, 92, 90)
print(p1.phy)
print(p1.chem)
print(p1.math)
s1.phy = 98
print(s1.percentage)
#This is the best way how we can change the percentage