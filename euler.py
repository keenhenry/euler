#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
import euler1_10

if __name__ == '__main__':
    ''' Program entry starts here:
    '''
    
    if len(sys.argv) != 2: 
	print 'Usage: python euler.py <p#>'
    else:
    	euler1_10.main()
