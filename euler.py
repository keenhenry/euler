#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
#import math

def int_factorization(n=232792560):
	'''A function that implements integer factorization
	'''

	# make a copy of n
	composite = n

	# initial prime factor
	pf = 2

	# a dictionary of prime factors
	pfs = {}

	# the main algorithm to find the prime factors of a number
	while n != 1:
		if n % pf == 0:
			n /= pf
			if pfs.has_key(pf):
				pfs[pf] += 1
			else:
				pfs[pf] = 1
		else:
			if pf < 3:
				pf += 1
			else:
				pf += 2

	primes = sorted(pfs.keys())
	
	# output result
	print composite, '=',
	for p in primes:
		if pfs[p] > 1:
			print str(p)+'^'+str(pfs.get(p)),
		else:	
			print p,

		if p == primes[-1]:
			print ''
		else:
			print 'X',
		

def p1():
	'''Solution to problem 1
	'''

	print str(sum(range(0, 1000, 3)) + sum(range(0, 1000, 5)) - \
		  sum(range(0, 1000, 15)))

def p2(maxlimit=4000000):
	'''Solution to problem 2
	'''
	
	def fib():
		a, b = 0, 1
		while b < maxlimit:
			yield b
			a, b = b, a+b
	
	s = 0
	for fn in fib():
		if fn%2 == 0:
			s += fn
	print s

def p3(n=600851475143):
	'''Solution to problem 3
	'''

	# initial largest prime factor (lpf)
	lpf = pf = 2

	# the main algorithm to find the largest prime factor of a number
	while n != 1:
		if n % pf == 0:
			n /= pf
			lpf = pf
		else:
			if pf < 3:
				pf += 1
			else:
				pf += 2

	# find the largest prime factor
	print 'The largest prime factor is:', lpf

def p5():
	'''Solution to problem 5
	'''

	base = 1*2*3*5*7*11*13*17*19
	print base*24

def p6():
	'''Solution to problem 6
	'''
	
	square_of_sum = sum(range(1,101))**2
	sum_of_squares = sum(map(lambda x: x*x, range(1, 101)))
	print abs(square_of_sum - sum_of_squares)


def main():
	
	func_list = {
		     'if': int_factorization,	
		     'p1': p1, 
		     'p2': p2, 
		     'p3': p3, 
		     'p5': p5, 
		     'p6': p6 
		    }
		    
	if len(sys.argv) != 2: 
		print 'Usage: python euler.py <p#>'
	elif not func_list.has_key(sys.argv[1]):
		print 'No solution to', sys.argv[1]
	else:
		func_list[sys.argv[1]]()	

if __name__ == '__main__':
	main()
