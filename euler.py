#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
import time
#import math

def prime(n):
	'''Primality testing function
	'''

	if n <= 1:
		return False
	if n < 4:
		return True
	if n%2==0:
		return False
	if n < 9:		# already excluded 4, 6, 8
		return True
	if n%3==0 or n%5==0:
		return False
	if n < 49:
		return True

	# prime numbers must be of the form 6k +/- 1
	p = 7
	while p**2 <= n:
		if n%p==0:		return False
		if (p+4)**2 > n:	return True
		if n%(p+4)==0:		return False
		p += 6		
	
	return True	

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

def p7(limit=10001):
	'''Solution to problem 7
	'''
	
	prime_list = [2, 3, 5, 7]

	# primality test
	def is_prime(n, list):
		for p in prime_list[2:]:
			if p*p > n:
				return True
			elif n%p == 0:	
				return False
	
	# generate prime numbers until hitting limit
	p = 11
	while len(prime_list) < limit:
		if is_prime(p, prime_list):
			prime_list.append(p)
		if is_prime(p+2, prime_list):
			prime_list.append(p+2)
		p += 6
		
	print prime_list[limit-1]

def p7_alt(limit=10001):
	'''Alternative solution to problem 7
	This solution is faster than p7 function for sure.
	'''

	count = 2
	candidate = p = 5
	
	#s = time.time()
	while 1:
		if prime(p):
			count += 1
			candidate = p
			if count == limit: break
		if prime(p+2):
			count += 1
			candidate = p+2
			if count == limit: break
		p += 6
	#e = time.time()

	print candidate#, str(e - s)

def main():
	
	func_list = {
		     'if': int_factorization,	
		     'p1': p1, 
		     'p2': p2, 
		     'p3': p3, 
		     'p5': p5, 
		     'p6': p6, 
		     'p7': p7,
		     'p7alt': p7_alt
		    }
		    
	if len(sys.argv) != 2: 
		print 'Usage: python euler.py <p#>'
	elif not func_list.has_key(sys.argv[1]):
		print 'No solution to', sys.argv[1]
	else:
		func_list[sys.argv[1]]()	

if __name__ == '__main__':
	main()
