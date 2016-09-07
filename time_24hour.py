#!/usr/bin/env python


def time24hr(tstr):
  meridiem = ""
  hour, minute = tstr.split(':')
  if 'am' in tstr:
    meridiem = 'am'
    minute = minute.translate(None, 'am')
    if hour == '12':
      hour = '00'
  else:
    meridiem = 'pm'
    minute = minute.translate(None, 'pm')
    if hour == '12':
      pass
    else:
      hour = str(int(hour) + 12)
  return hour + minute + 'hr'


print time24hr('12:34am')
#  '0034hr'
print time24hr('12:15pm')
# '1215hr'
