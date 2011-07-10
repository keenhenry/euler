#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
#import cProfile
import euler1_10
import euler11_20
import euler21_30
import euler31_40
import euler41_50
import euler51_60

if __name__ == '__main__':
    ''' Program entry starts here:
    '''
    
    if len(sys.argv) != 2: 
	print 'Usage: python euler.py <p#>'
    elif sys.argv[1] <= 'p10':
    	euler1_10.main()
    elif sys.argv[1] <= 'p20':	
	euler11_20.main()
    elif sys.argv[1] <= 'p30':	
	euler21_30.main()
    elif sys.argv[1] <= 'p40':	
	euler31_40.main()
    elif sys.argv[1] <= 'p50':	
	euler41_50.main()
    elif sys.argv[1] <= 'p60':	
	euler51_60.main()

