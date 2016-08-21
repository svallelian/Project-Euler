"""
Created on Aug 21 2016

Project Euler Problem 013
Find the first ten digits of the sum of the given one-hundred 
50-digit numbers.

@author: sarahv
"""
import numpy as np

num_digits = 50;
firstdigs = 10;
sums_digits = np.zeros(num_digits);

def combinedigits(sums_digits):
    " Given an array of sums in each digit place, form the total sum "
    N = len(sums_digits);
    sum_as_array = np.zeros(num_digits);
    for k in range(N):
        current = sums_digits[N-k-1];
        currentstr = str(int(current));
        currentlen = len(currentstr);
        
    return totalsum

with open('Problem013.txt') as input_file:
    for line in input_file:
        " Verify the line has 50 characters "
        line = line.strip();
        if (len(line) != num_digits):
            print('Error: num_digits does not match txt data. \n');
            break
        " Add the line's digits to the array of the sum in each place "
        for k in range(num_digits):
            sums_digits[k] += int(line[k]);


answer = combinedigits(sums_digits);    