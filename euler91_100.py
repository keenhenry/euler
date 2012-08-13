#!/usr/bin/python

""" Project Euler Solutions: Problem 91 - 100
"""

import sys
import time

def p97():
    '''Solution to problem 97

    @2012.08.11 This is brute force solution. It takes about 10 secs to run. Try think a better solution.
    '''

    r, d = 28433, 10**10

    for i in xrange(1, 7830458):
        r *= 2
        if len(str(r)) >= 10: r = r%d
 
    print str(r+1)

def main():
    '''Main program of module euler91_100 
    '''

    func_list = {
        'p97': p97
    }
		    
    if func_list.has_key(sys.argv[1]):
	    func_list[sys.argv[1]]()	
    else:
	    print 'No solution to', sys.argv[1]
