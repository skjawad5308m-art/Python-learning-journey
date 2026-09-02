f = open("world.txt", "r+")
f.write("The world")
print(f.read())
f.close()

f= open("city.txt", "w+")
print(f.read())
f.write("I live in Dhaka city with my family")
f.close()

f= open("occupation.txt", "a+")
print(f.read())
f.write("and that is my occupation")
f.close()