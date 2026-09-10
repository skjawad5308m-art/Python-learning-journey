class School:
    varS = "My school was Dhaka Residential Model college from where I have passed SSC or 10th grade"
class College:
    varC = "I am also currently studying in Dhaka Residential Model College from where I will pass HSC or 12th grade "
class University(School, College):
    varU = "I am hoping to study in a foreign University with scholarship "
print(University.varS)
print(University.varU)
print(University.varU)