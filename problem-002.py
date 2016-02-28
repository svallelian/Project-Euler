
"""
Created on Jan 25 2016

Project Euler Problem 002
Find the sum of all Fibonnaci numbers which are less than maxnumber and even

@author: sarahv
"""

maxnumber=4e6

fiblist=[1,2]
while fiblist[-1] < maxnumber:
    fiblist.append(fiblist[-1]+fiblist[-2])

print sum([x for x in fiblist if x % 2 == 0])