#!/usr/bin/env python

def add_them(a, b, c):
  return a + b + c

def Fitness(a, b, c):
  if a >= 4 and b >= 4 and c >= 4 and add_them(a, b, c) >= 13:
    return 'Gold'
  elif a >=3 and b >= 3 and c >= 3 and add_them(a, b, c) >= 10:
    return 'Silver'
  elif a >=2 and b >= 2 and c >= 2 and add_them(a, b, c) >= 7:
    return 'Pass'
  else:
    return 'Fail'


print Fitness(4,5,4)
print Fitness(4,4,4)
print Fitness(1,5,5)
print Fitness(2,2,5)
