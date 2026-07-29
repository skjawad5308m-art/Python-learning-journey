num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in num :
    print(val)
    print(type(val))
    print(type(num))
    print(len(num))
    print(len(num[1:]))
    print(len(num[:2]))
    print(len(num[1:4]))
    print(len(num[5: 3]))
    print(len(num[-1:]))
    print(len(num[-3:-5]))
else:
    print("THE LOOP HAS ENDED")

fruits = ["APPLE", "BANANA", "LICHI", "ORANGE"]

for val in fruits:
    print(val)
    print(type(val))
    print(type(fruits))
    print(len(fruits))
    print(len(fruits[1:]))
    print(len(fruits[:2]))
    print(len(fruits[1:4]))
    print(len(fruits[5: 3]))
    print(len(fruits[-1:]))
    print(len(fruits[-3:-5]))
else:
    print("THE LOOP ENDS HERE")

str1 = "MY NAME IS MOHAMMAD SUJNAIN JAWAD"

for char in str1 :
    print(char)
    print(type(char))
    print(type(str1))
    print(len(str1))
    print(len(str1[1:]))
    print(len(str1[:2]))
    print(len(str1[1:4]))
    print(len(str1[5: 3]))
    print(len(str1[-1:]))
    print(len(str1[-3:-5]))
else:
    print("THIS IS THE END OF THE LOOP")

str2 = "THE WORLD IS VERY BEAUTIFUL"

for char in str2 :
    print(char)
    print(type(char))
    print(type(str2))
    print(len(str2))
    print(len(str2[1:]))
    print(len(str2[:2]))
    print(len(str2[1:4]))
    print(len(str2[5: 3]))
    print(len(str2[-1:]))
    print(len(str2[-3:-5]))
    if(char == "B"):
        print("B has founded")
        break
    print(char)