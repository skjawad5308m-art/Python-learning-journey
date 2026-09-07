class Mobile:
    def __init__(price):
        price.iphone17 = 1099
        price.iphone16 = 729
m1 = Mobile()
print(m1.iphone17)
print(m1.iphone16)

budget = float(input("Enter your budget:"))
if budget >= m1.iphone17:
    print("I will purchase iphone 17" )
elif budget != m1.iphone17:
    print("I do not have enough money to take iphone 17 instead i will take iphone 16")