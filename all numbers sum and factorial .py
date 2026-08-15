n = 20

sum = 0
for i in range(1, n+1):
    sum += i
    print("total sum", sum)

n = 20

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
    print("total sum", sum)

n2 = 10
fact = 1
for i in range(1, n2 + 1):
    fact *= i
    i += 1
    print("total factorial", fact)

n2 = 10
fact = 1
i = 1
while i <= n2:
    fact *= i
i += 1
print("total factorial", fact)