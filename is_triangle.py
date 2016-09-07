#!/usr/bin/env python

def isTriangle(x,y,z):
  list2 = [x, y, z]
  list1 = sorted(list2)
  if min(list1) <= 0:
    return False
  elif list1[0] + list1[1] > list1[2]:
    return True
  else:
    return False


print isTriangle(3,4,5)
print isTriangle(1,3,1)
print isTriangle(1,2,2)
