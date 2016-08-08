
"""
Created on Mar 14 2016

Project Euler Problem 010
Find the sum of all the primes below two million.

@author: sarahv
"""

maxnum=2000000;

def relativelyprime(n,plist):
    """ Returns False if n is divisible by anything in plist, otherwise returns True """
    for p in plist:
        if n % p == 0:
            return False
    return True
    
def findNextPrime(plist):
    """ Appends the next largest prime to the input list """
    current=plist[-1]+1;
    while relativelyprime(current,plist)==False:
        current+=1;
        """ When relativelyprime(current,plist) is true, current is prime """
    plist.append(current);
    return plist
    
def findSumPrimesLess(maxnum):
    plist=[2];
    total=2;
    while plist[-1] < maxnum:
        plist = findNextPrime(plist);
        if plist[-1] < maxnum:
            total += plist[-1];
    return total
    
output=findSumPrimesLess(maxnum);