
"""
Created on Aug 7 2016

Project Euler Problem 011
Find the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid

@author: sarahv
"""
import numpy as np

" Extract the grid as an array "
array = np.loadtxt('Problem011.txt');

def maxUDLRProduct(array,adj):
    " Given an array and # adjacent entries, find largest product "
    " in the up/down or left/right direction "
    N = len(array);
    maxprod = 0;
    if adj >= N:
        print('Error: adj is larger than grid size. \n');
        return
    for k in range(N-adj+1):
        tempUD = array[k,:];
        tempLR = array[:,k];
        " Compute the column/rowwise products "
        for i in range(adj-1):
            tempUD = tempUD*array[k+i+1,:];
            tempLR = tempLR*array[:,k+i+1];
        if max(max(tempUD),max(tempLR)) > maxprod:
            maxprod = max(max(tempUD),max(tempLR));
    return maxprod
    
def maxDiagonalProduct(array,adj):
    " Given an array and # adjacent entries, find largest product "
    " in a diagonal direction "
    " We assume the array is square "
    N = len(array);
    maxprod = 0;
    if adj >= N:
        print('Error: adj is larger than grid size. \n');
        return
    for k in range(N-adj+1):
        tempL = array[k,0:N-adj+1];
        tempR = array[k,adj-1:N];
        " Compute the rowwise product of the adj many columns right of column k "
        for i in range(adj-1):
            tempL = tempL*array[k+i+1,i+1:N-adj+i+2];
            tempR = tempR*array[k+i+1,adj-1-i-1:N-i-1];
        if max(max(tempL),max(tempR)) > maxprod:
            maxprod = max(max(tempL),max(tempR));
    return maxprod
    
answer = max(maxUDLRProduct(array,4), maxDiagonalProduct(array,4));
