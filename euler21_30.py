#!/usr/bin/python

""" Project Euler Solutions: Problem 21 - 30
"""

import sys
import time
#import math

# function to generate fibonacci numbers: a generator	
def fib():
    a, b, i = 0, 1, 1
    while True:
	yield b, i
	a, b, i = b, a+b, i+1

def p25():
    '''Solution to problem 25 
    '''
    
    for fn, i in fib():
	if len(str(fn)) >= 1000:
	    print i
	    break

def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
        'p25': p25    
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
