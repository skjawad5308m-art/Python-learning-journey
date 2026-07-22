student = {
    "Name" : "Jawad",
    "Age" : 17,
    "Institution" : "Dhaka Residential Model College",
    "Class" : 10,
    "Email": "skjawad5308m@gmail.com",
    "subjects" : {
        "Physcis" : 85,
        "Chemistry" : 90,
        "Higher Math" : 86
    }


}

print(student)
print(type(student))
print(student["subjects"])
print(type(student["subjects"]))
student["Name"] = "MD.Sujnain Jawad"
print(student)
student["subjects"]["Physics"] = 87
print(student)
print(student["subjects"])