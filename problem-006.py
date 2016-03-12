
"""
Created on Mar 11 2016

Project Euler Problem 006
Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.

@author: sarahv
"""

N=100;

sumofsquares=sum([x**2 for x in range(1,N+1)]);
squareofsum=sum([x for x in range(1,N+1)])**2;

diff=squareofsum-sumofsquares;