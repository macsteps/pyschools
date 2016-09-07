#!/usr/bin/env python
# purpose: convert from military time to civilian time

def time12hr(tstr):
  if (tstr[0] + tstr[1] == '00'):
    new_tstr = '12' + tstr[2] + tstr[3]
    meridiem = " a.m."
    return str(new_tstr)[0] + str(new_tstr)[1] + ":" + str(new_tstr)[2] + str(new_tstr)[3] + meridiem
  elif int(tstr) < 1200:
    meridiem = " a.m."
    return str(tstr)[0] + str(tstr)[1] + ":" + str(tstr)[2] + str(tstr)[3] + meridiem
  elif int(tstr) > 1259:
    meridiem = " p.m."
    tstr = int(tstr) - 1200
    if len(str(tstr)) == 4:
      return str(tstr)[0] + str(tstr)[1] + ":" + str(tstr)[2] + str(tstr)[3] + meridiem 
    else: 
      return str(tstr)[0] + ":" + str(tstr)[1] + str(tstr)[2] + meridiem
  else:
     meridiem = " p.m."
     return str(tstr)[0] + str(tstr)[1] + ":" + str(tstr)[2] + str(tstr)[3] + meridiem 

print time12hr('1619')
    #'4:19 p.m.'
print time12hr('1200')
    #'12:00 p.m.'
print time12hr('1020')
    #'10:20 a.m.' 
print time12hr('1202')
print time12hr('1200')
print time12hr('0059')
print time12hr('0000')

