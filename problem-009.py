
"""
Created on Mar 14 2016

Project Euler Problem 009
Find the product of the Pythagorean triple satisfying a+b+c=1000

@author: sarahv
"""

abcsum=1000;

for a in range(1,int(abcsum/3)+1):
    if ((abcsum**2)/2) % (abcsum-a)==0:
        b=abcsum - (abcsum**2)/2/(abcsum-a);
        c=abcsum - a-b;
        abcprod=a*b*c;

