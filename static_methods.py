class Student:
    name = "Jawad"
    def __init__(self, name , marks1, marks2, marks3, subjects):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.subjects = subjects
    @staticmethod
    def avg(marks1, marks2, marks3):
        avg = (marks1 + marks2 + marks3) /3
        return avg
s1 = Student("Jawad", 86, 85, 83, 3)
print(s1.name)
print(s1.marks1)
print(s1.marks2)
print(s1.marks3)
print(s1.subjects)
print(s1.avg(s1.marks1 , s1.marks2 , s1.marks3 ))
