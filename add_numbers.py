#!/usr/bin/env python

def addEvenNumbers(start, end):
  x = 0
  for i in range(start, end + 1):
    if i % 2 == 0:
      x += i
  return x

print addEvenNumbers(3, 7)
print addEvenNumbers(5, 12)
