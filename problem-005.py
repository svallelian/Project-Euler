
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
    """ Returns the product and list of factors of all natural numbers <= n, where n > 3 """
    y=[]
    prod=1
    for x in range(1,n+1):
        if x==1 or x==2 or x==3:
            y.append(x)
            prod*=x
        else:
            fac=primefactors(x)
            remaining=y[:]
            for k in range(0,len(fac)):
                """ Go through each factor of the current digit and save any extras """
                if fac[k] in remaining:
                    remaining.remove(fac[k])
                else:
                    y.append(fac[k])
                    prod*=fac[k]
            
    return y, prod
       
factors, prod=factorizeall(n)
