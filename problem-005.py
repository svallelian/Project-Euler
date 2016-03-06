
"""
Created on Mar 6 2016

Project Euler Problem 005
Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

@author: sarahv
"""

n=20

def primefactors(n):
    """ Returns prime factorization of n > 3"""
    """ Start with the smallest prime and factor out primes smallest to largest """
    i=2
    factors=[]
    while (i*i <= n):
        if (n%i == 0):
            """ i is a factor of n, update n """
            n //= i
            factors.append(i)
        else:
            """ i is not a factor of n, update i """
            i += 1
    """ when while terminates, n has no other prime factors """
    factors.append(n)
    return factors
    
def factorizeall(n):
    """ Returns the list of factors of all natural numbers <= n, where n > 3 """
    y=[]
    for x in range(1,n+1):
        if x==1 or x==2 or x==3:
            y.append([x])
        else:
            y.append(primefactors(x))
    return y
       
output=factorizeall(n)
