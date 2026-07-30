tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

for num in tup:
    print(num)
    print(len(tup))
    print(type(num))

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49,121, 144, 169, 49, 49)
x = 49
idx = 0
for val in nums:
    if(val == x):
        print("FOUND AT idx", idx)
    else:
        print("STILL SEARCHING......")
    idx += 1