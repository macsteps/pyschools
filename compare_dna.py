#!/usr/bin/env python

def pairwiseScore(seqA, seqB):
  match = ""
  last = False
  score = 0
  for x in range(len(seqA)):
    if seqA[x] == seqB[x]:
      if last == True:
        score += 3
      else:
        score += 1
      match += "|"
      last = True
    else:
      score -= 1
      match += " " 
      last = False 
  return seqA + "\n" + match + "\n" + seqB + "\n" + "Score: %d" % score

print pairwiseScore("ATTCGT", "ATCTAT")
#    ATTCGT
#    ||   |
#    ATCTAT
#    Score: 2 
print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")
#    GATAAATCTGGTCT
#     ||  |||  |   
#    CATTCATCATGCAA
#    Score: 4 
