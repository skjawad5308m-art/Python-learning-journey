i = 0
while i <= 1000:
    print(i)
    if(i == 998):
        break
    i += 1
print("The loop ends here")


i2 = 100
while i2 >= 0:
    if(i2 == 98):
        i2 -= 1
        continue
    print(i2)
    i2 = i2 - 1
print("The loop ends here")

i3 = 1
while i3 <= 1000:
    if(i3 % 2 == 0):
        i3 += 1
        continue
    print(i3)
    i3 += 1
print("The loop ends here")

i4 = 1
while i4 <= 100:
    if(i4 % 2 != 0):
        i4 += 1
        continue
    print(i4)
    i4 += 1
print("This is the limit of the loop")
