#!/usr/bin/env python

def generateNumber(start, end, step):
  lst = []
  if step > 0:
    end += 1
  else:
    end -= 1
  for i in range(start, end, step):
    lst.append(i)
  return lst


print generateNumber(2, 10, 2)
print generateNumber(10, 10, 1)
print generateNumber(20, 0, -3)
print generateNumber(15, 6, -2)
