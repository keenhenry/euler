#!/usr/bin/python

""" Project Euler Solutions: Problem 51 - 60
"""

import sys
import time

def p52():
    '''Solution to problem 52

    In this problem, I used brute force to break it. It runs within a second.
    However, this problem can be solved trivially by knowing that 1/7 has that 
    cicular property.
    '''
  
    def circular(n=125874):
    	"Test if n is circular within 2x, 3x, 4x, 5x, 6x mutitples"

    	ans, digits = True, set(str(n))	   # a set of digits of original number
	for i in xrange(2, 7):
	    t = n * i
	    t_digits = set(str(t))
	    if t_digits != digits: 
	    	ans = False
		break
	return ans

    x, not_found = 101, True
    while not_found:
    	if len(str(x))==len(str(6*x)) and circular(x): not_found = False
	else: x += 1
    print x

def main():
    '''Main program of module euler51_60 
    '''

    func_list = {
        'p52': p52
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
