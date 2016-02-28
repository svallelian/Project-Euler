"""
Created on Jan 25 2016

Project Euler Problem 001
Find the sum of all numbers less than maxnumber which are divisible by either firstprime or secondprime


@author: sarahv
"""

maxnumber=1000
firstprime=3
secondprime=5

print sum([x for x in range(maxnumber) if x % firstprime == 0 or x % secondprime == 0])