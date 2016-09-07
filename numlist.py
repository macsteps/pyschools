#!/usr/bin/env python

def getSumOfLastDigits(numList): 
  sum_of_list = 0
  for i in numList:
    sum_of_list += int(str(i)[-1:])
  return sum_of_list

print getSumOfLastDigits([2, 23, 114])
print getSumOfLastDigits([1, 23, 456])

