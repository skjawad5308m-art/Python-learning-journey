list1 = [2, 3, 4, 3, 2]
list2 = [2, 3, 4, 5, 6]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrom")
else:
    print("Not Palindrom")