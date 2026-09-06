class Student:
    college_name = "Dhaka Residential Model College."

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 = Student("Anik", "11th grade")
print(s1.name, s1.college_name)
print(s1.grade, s1.college_name)
s2 = Student("Utsa", "11th grade")
print(s2.name, s2.college_name)
print(s2.grade, s2.college_name)
s3 = Student("Tanfiz", "11th grade")
print(s3.name, s3.grade, s3.college_name)
s4 = Student("Zarif", "11th grade")
print(s4.name, s4.grade, s4.college_name)