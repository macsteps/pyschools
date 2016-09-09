#!/usr/bin/env python

def sumOfDigit(num):
  x = 0
  str_num = str(num)
  for i in range(len(str_num)):
    x += int(str_num[i])
  return x

print sumOfDigit(123)
print sumOfDigit(234)
print sumOfDigit(1000)
print sumOfDigit(1001)
