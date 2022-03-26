def fast_pow_iter(m, n):
    if n % 2 == 0:
        res = 1
        count = 0
        while count < n / 2:
            res = res * m
            count += 1
        return res * res
    elif n % 2 != 0:
        res = 1
        count = 0
        while count < (n - 1):
            res = res * m
            count += 1
        return m * res

print(fast_pow_iter(2, 3))

