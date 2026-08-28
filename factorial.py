n = 10
fact = 1
for i in range(1 , n+1):
    fact *= i
print(fact)

def calc_fact2(n2):
    fact2 = 1
    for i2 in range(1, n2+1):
        fact2 *= i2
    print(fact2)
calc_fact2(8)
