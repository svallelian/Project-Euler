
"""
Created on Mar 5 2016

Project Euler Problem 004
Find the largest palindrome made from the product of two 3-digit numbers.

@author: sarahv
"""

num_digits=3

def ispalindrome(num):
    """ Returns true if input number is a palindrome, otherwise false """
    num=str(num)
    length=len(num)
    l=int(length/2)
    for k in range(0,l):
        if num[k] != num[length-1-k]:
            return False
    return True
    

def listprods(num_digits):
    """ Returns a sorted list of palindromes formed as products of two numbers with input number of digits """
    largest='9'
    smallest='1'
    for k in range(1,num_digits):
        largest+='9'
        smallest+='0'
    largest=int(largest)
    smallest=int(smallest)
    y=[]
    for k in range(smallest,largest+1):
        for j in range(k,largest+1):
            if ispalindrome(j*k):
                y.append(j*k)
    y.sort()
    return y
    
output=listprods(num_digits)

answer=output[len(output)-1]