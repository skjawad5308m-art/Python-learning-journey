set1 = {1, 2, 3, 5, 6, 8}
print(set1)
print(len(set1))
print(type(set1))

set2 = {2, 4, 5, 7, 8}
print(set2)
print(type(set2))
print(len(set2))

set3 = set1.union(set2)
print(set3)
print(type(set3))
print(len(set3))

set4 = set1.intersection(set2)
print(set4)
print(len(set4))
print(type(set4))

set5 = set1.difference(set2)
print(set5)
print(type(set5))
print(len(set5))

set6 = set2.difference(set1)
print(set6)
print(type(set6))
print(len(set6))

set7 = set1.symmetric_difference(set2)
print(set7)
print(type(set7))
print(len(set7))

set8 = set2.symmetric_difference(set1)
print(set8)
print(type(set8))
print(len(set8))

set9 = set1.difference_update(set2)
print(set9)

set10 = set1.symmetric_difference_update(set2)
print(set10)

set11 = set2.difference_update(set1)
print(set11)

set12 = set2.symmetric_difference(set1)
print(set12)
print(len(set12))

set13 = set1.discard(set2)
print(set13)
print(len(set13))