def pow(a, b):
    res = 1
    count = 0
    while count < abs(b):
        res *= a
        count += 1
    if b > 0:
        return res
    elif b < 0:
        return 1 / res
    elif b == o:
        return 1
    elif a == 0 and b < 0:
        return "wrong expression"
