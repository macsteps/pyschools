#!/usr/bin/env python

def addNumbers(num):
  x = 0
  for i in range(num+1):
    x += i
  return x

print addNumbers(4)
