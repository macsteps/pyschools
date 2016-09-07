#!/usr/bin/env python

def BMI(weight, height):
  bmi = float(weight) / float(height * height)
  return "%.1f" % bmi

print BMI(63, 1.7)
print BMI(110, 2)

