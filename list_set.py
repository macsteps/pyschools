#!/usr/bin/env

def genSet(nums): 
    new_list = list(set(nums))
    new_list.sort()
    return new_list

print genSet([5,4,8,4,9,8])
print genSet([3,-2,-1,-1,3,-2,0])
