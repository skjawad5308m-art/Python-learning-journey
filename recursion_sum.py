def calc_sum(n):
    if (n == 0 or n == 1):
        return 1
    return calc_sum(n-1) + n
print(calc_sum(5))

def calc_diff(n):
    if(n== 0 or n == 1):
        return 1
    return(calc_diff(n-1))
print(calc_diff(5))

def calc_multiply(n):
    if (n == 0 or n == 1):
        return 1
    return calc_multiply(n)
print(calc_multiply(5))


def calc_dev(n):
    if (n == 0 or n == 1):
        return 1
    return calc_dev(n / 1)
print(calc_dev(5))