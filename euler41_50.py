#!/usr/bin/python

""" Project Euler Solutions: Problem 21 - 30
"""

import sys
import time
#import math

def p48(n=1000):
    '''Solution to problem 48
    '''

    print str(sum(map(lambda x: x**x, range(1, n+1))))[-10:]
    
def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
        'p48': p48
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
