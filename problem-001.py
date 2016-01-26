"""
Created on Jan 25 2016

@author: sarahv
"""

maxnumber=1000

print sum([x for x in range(maxnumber) if x % 3 == 0 or x % 5 == 0])