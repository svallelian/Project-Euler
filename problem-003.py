
"""
Created on Jan 25 2016

Project Euler Problem 003
Find the largest prime factor of the given number

@author: sarahv
"""

given=600851475143


def largestfactor(n):
    """ Returns largest prime factor <= n """
    """ Start with the smallest prime and factor out primes smallest to largest """
    i=2
    while (i*i <= n):
        if (n%i == 0):
            """ i is a factor of n, update n """
            n //= i
        else:
            """ i is not a factor of n, update i """
            i += 1
    """ when while terminates, n has no other prime factors """
    return n
    
output=largestfactor(given)