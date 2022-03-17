def cubic(m):
    res = 1
    while abs(res ** 3) - m <= 0.0001:
        res = ((m / (res ** 2)) + (2 ** res)) / 3
    return res 

