def show (n):
    if (n == -101):
        return
    print(n)
    show(n -1)
    print("This is the end")
show(0)

def show(n2):
    if(n2 == 100):
        return
    print(n2)
    show(n2 +1)
    print("END")
show(0)