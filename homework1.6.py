def amount_nums(a, b):
  sum_num = 0
  if a < b:
    while a <= b:
      sum_num += a 
      a += 1
    return(sum_num)
  else:
    while b <= a:
      sum_num += b 
      b += 1
    return(sum_num)

