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
	'p36': p36 
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
