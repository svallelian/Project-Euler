
"""
Created on Aug 21 2016

Project Euler Problem 012
Find the the value of the first triangle number to have 
over five hundred divisors.

@author: sarahv
"""

num_divisors = 500;

def divisorlist(N):
    """ Given a positive integer N, construct a sorted list of its divisors """
    divlist = [1,N];
    p = 2;
    while (p < divlist[-1]):
        """ Determine if p is a divisor; if so, append divlist """
        if (N%p == 0):
            divlist.append(p);
            if (p != int(N/p)):
                divlist.append(int(N/p));
        p += 1;
    return sorted(divlist), len(divlist)
    
def findtridivs(num_divisors):
    tri = 3;
    generator = 2;
    divlist, listlen = divisorlist(tri);
    while (listlen < num_divisors):
        generator +=1;
        tri = sum(k for k in range(1,generator));
        divlist, listlen = divisorlist(tri);
    return tri
    
test = findtridivs(num_divisors)