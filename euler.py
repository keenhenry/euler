#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
import euler1_10
import euler11_20

if __name__ == '__main__':
    ''' Program entry starts here:
    '''
    
    if len(sys.argv) != 2: 
	print 'Usage: python euler.py <p#>'
    elif sys.argv[1] <= 'p10':
    	euler1_10.main()
    elif sys.argv[1] <= 'p20':	
	euler11_20.main()
