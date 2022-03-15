def my_nums(a1,a2,a3):
  if (a1 > a3) and (a2 > a3):
    return (a1 ** 2) + (a2 ** 2)  
  if (a1 > a2) and (a3 > a2):
    return (a1 ** 2) + (a3 ** 2)
  if (a3 > a1) and (a2 > a1):
    return (a3 ** 2) + (a2 ** 2)

print(my_nums(2, 4, 56,))
