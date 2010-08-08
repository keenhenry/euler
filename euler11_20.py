#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
import time
#import math

def p16(n=2**1000):
    '''Solution to problem 16
    This solution outputs the answer in less than 0.0006 second!
    And it is a one liner!!! This is really good python!
    '''
    print sum(map(int, list(str(n))))

def p20(n=100):
    '''Solution to problem 20
    Again it is a one liner!!! This is really good python!
    '''

    #n_fac = reduce(lambda x,y: x*y, xrange(1,n))
    print sum(map(int, list(str(reduce(lambda x,y: x*y, xrange(1,n))))))

def main():
    '''Main program of module euler11_20 
    '''

    func_list = {
        'p16': p16, 'p20': p20
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
