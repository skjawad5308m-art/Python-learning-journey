def show (n):
    if (n == -101):
        return
    print(n)
    show(n -1)
show(0)

def show(n2):
    if(n2 == 100):
        return
    print(n2)
    show(n2 +1)
show(0)