def my_func(n):
    if n < 0 or type(n) != int:
        return "incorrect number"
    elif n < 3:
        return n
    elif n >= 3:
        return my_func(n - 1) + my_func(n - 2) + my_func(n - 3)
