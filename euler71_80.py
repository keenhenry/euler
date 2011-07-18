#!/usr/bin/python

""" Project Euler Solutions: Problem 71 - 80
"""

import sys
import time

def p76():
    '''Solution to problem 76

    This problem is identical to problem 31!
    '''
 
    print 'Check solution for problem 31'

def main():
    '''Main program of module euler51_60 
    '''

    func_list = {
        'p76': p76
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
