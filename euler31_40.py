#!/usr/bin/python

""" Project Euler Solutions: Problem 31 - 40
"""

import sys
import time

def fib():
    '''A function to generate fibonacci numbers: a generator	
    '''
    a, b, i = 0, 1, 1
    while True:
	yield b, i
	a, b, i = b, a+b, i+1

def ydigits(num=0):
    '''A function to extract the digits of an integer.
    '''

    while num!=0:
    	d, num = num%10, num/10
	yield d

def dec2bin(n):
    '''A function to convert an integer from decimal to binary representation (string)

    There are 1000 ways to do this. Here I am just showing one of it.
    '''
    
    s = ""
    
    while n: 
        s = "1" + s if (n & 1) else "0" + s
        n = (n >> 1)
    return s

def is_palindrome(n):
    '''A function to check palindrome.
    '''
    
    s = str(n) if not isinstance(n, str) else n 
    return s[::-1] == s

def factorial(n):
    '''A function to calculate the factorial of n.
    '''

    ans = 1
    for i in xrange(1, n+1): ans *= i
    return ans	

def p34(upper=2540160):
    '''Solution to problem 34 
    
    This problem is similar to problem 30. The key is to find the upper bound.
    upper==2540160==7x9!
    '''
   
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s = 0    # sum of all numbers which are equal to the sum of factorial of their digits.
    for i in xrange(100, upper):
    	sum_of_factorial_of_digits = 0
	for d in ydigits(i): sum_of_factorial_of_digits += facts[d]
    	if i == sum_of_factorial_of_digits: s += i
    print s

def p36(limit=1000000):
    '''Solution to problem 36 
    '''
    
    s = 0    # the sum of all numbers which are palindrom in base10 and base2
    for i in xrange(1, limit, 2):    # only ODD numbers can be candidates!	
        if is_palindrome(i) and is_palindrome(bin(i)[2:]): s += i
        #if is_palindrome(i) and is_palindrome(dec2bin(i)): s += i
    print s

def main():
    '''Main program of module euler31_40 
    '''

    func_list = {
	'p34': p34, 'p36': p36 
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
