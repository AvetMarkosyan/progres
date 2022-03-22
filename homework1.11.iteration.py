def my_func(n):
    a = 0
    b = 1
    c = 2
    while n > 0:
        tmp = a
        a = a + b
        b = b + c
        c = tmp
        n -= 1
    return c

        
