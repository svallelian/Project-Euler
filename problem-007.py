
"""
Created on Mar 11 2016

Project Euler Problem 007
Find the Nth largest prime number.

@author: sarahv
"""

N=10001;

def relativelyprime(n,plist):
    """ Returns False if n is divisible by anything in plist, otherwise returns True """
    for p in plist:
        if n % p == 0:
            return False
    return True
    
def findNthprime(N):
    """ Returns the Nth largest prime, where the first is 2 """
    plist=[2];
    length=1;
    while length < N:
        """ Find the next largest prime """
        current=plist[-1]+1;
        while relativelyprime(current,plist)==False:
            current+=1;
        """ When relativelyprime(current,plist) is true, current is prime """
        plist.append(current);
        length+=1;
    """ When length = N, plist[-1] is the Nth largest prime """
    return plist[-1]
    
output=findNthprime(N);