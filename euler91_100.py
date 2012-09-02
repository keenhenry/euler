#!/usr/bin/python

""" Project Euler Solutions: Problem 91 - 100
"""

import sys
import time

def fast_pow(a, b):
    '''A function to calculate a**b quickly (a and b are both natural numbers)

    Assume b > 0!

    Python probably implement a**b using this algorithm internally, however it is 
    still good to have some idea of how this can be done programatically in O(log n)

    Idea is from http://www.osix.net/modules/article/?id=696
    '''

    # if b < 0: 
    # throw some error if b < 0
        
    if b == 0: return 1
    if a == 0: return 0

    # b > 0
    return fast_pow(a*a, b/2) if b%2 == 0 else a*fast_pow(a*a, b/2)


def p97():
    '''Solution to problem 97

    @2012.08.11 This is brute force solution. It takes about 10 secs to run. Try think a better solution.
    @2012.08.11 Now it runs less than tenth of a second, but this is taking advantage of python, not a smart algorithm.
    @2012.09.02 A logarithmic algorithm is used, run in a fraction of a second!
    '''

    ### Brute force solution ###

    # r, d = 28433, 10**10

    # for i in xrange(1, 7830458):
    #     r *= 2
    #     if len(str(r)) >= 10: r = r%d
 
    # print str(r+1)

    ### python knows how to calculate it quickly?!  No algorithm here ###
    # print ((28433 << 7830457)+1) % 10**10

    ### now a real algorithm to solve this problem ###
    print (28433*fast_pow(2,7830457)+1) % 10**10

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
