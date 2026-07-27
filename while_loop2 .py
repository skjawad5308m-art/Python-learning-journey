i = 1
while i <= 1000:
    print(i)
    i = i + 1
print("The loop has ended")

i2 = 1000
while i2 >= 1:
    print(i2)
    i2 = i2 -1
print("The loop ends here")

i3 = 1
while i3 <= 10:
    print(50 *i3)
    i3 = i3 + 1
print("This is the end of the loop")

n = int(input("Enter the number:"))
i4 = 1000
while i4 >= 1:
    print(i4 / n)
    i4 = i4 - 1
print("You have crossed the limit of the loop")

n2 = int(input("Enter the number:"))
i5 = 1
while i5 <= 10:
    print(i5 ** n2)
    i5 = i5 + 1
print("This is the deadend of the loop")

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
idx = 0
while idx < len(nums):
    print(idx)
    print(nums[idx])
    idx += 1

nums2 = (1, 2, 4, 9, 16, 25, 36, 49)

x = 9
i6 = 0
while i6 < len(nums2):
    if(nums2[i6] == x):
        print("FOUND at idx", i6)
        i6 = i6 + 1
    else:
        print("STILL FINDING .......")
        i6 += 1