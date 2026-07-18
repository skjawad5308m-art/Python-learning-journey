num = int(input("Enter the number:"))
if(num%2 ==0):
    print("THE NUMBER IS EVEN")
else:
    print("THE NUMBER IS ODD")

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
d = int(input("Enter the fourth number:"))
if(a >b and a > c and a > d):
    print("first number is the greatest number",a)
elif(b > a and b > c and b > d):
    print("second is the greatest number",b)
elif(c > a and c > b and c > d):
    print("third is the greatest number",c)
else:
    print("fourth is the greatest number",d)

x = int(input("Enter the number:"))
if(x%7 ==0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")