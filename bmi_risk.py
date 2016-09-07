#!/usr/bin/env python

def msg(bmi, risk):
  return 'Your BMI is %.1f (%s).' % (bmi, risk)

def HealthScreen(weight, height):
  bmi = float(weight) / float((height * height))
  if bmi >= 27.5:
    return msg(bmi, 'High Risk')
  elif bmi >= 23:
    return msg(bmi, 'Moderate Risk')
  elif bmi >= 18.5:
    return msg(bmi, 'Low Risk')
  else:
    return msg(bmi, 'Risk of nutritional deficiency diseases')
    
print HealthScreen(85, 1.75)
print HealthScreen(68, 1.65)
print HealthScreen(60, 1.63)
print HealthScreen(40,1.58)
print HealthScreen(80,1.83)
