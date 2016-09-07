#!/usr/bin/env python

def percent(value, total):
  p = (float(value) / float(total)) * 100
  return int(p)

print percent(46, 90)
print percent(51, 51)
print percent(63, 12)

