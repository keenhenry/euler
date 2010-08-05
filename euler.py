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
		
def sieve(n=100000):
	'''The Sieve of Eratosthenes algorithm
	'''
	l = range(1, n, 2)
	l[0] = 2

	k, p = 1, 3
	while p*p <= n:
		for e in l[k+1:]:
			if e%p == 0:
				l.remove(e)
		k += 1		
		p = l[k]		
			
	print 'done'

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

def p4():
	'''Solution to problem 4
	'''

	# a function to check palindrome
	def is_palindrome(n):
		s = str(n)
		i, j = 0, len(s)-1
		while i < j:
			if s[i] != s[j]: return False
			i += 1
			j -= 1
	
		return True

	# using brute-force method to find answer
	# two integers must be between 100~999
	# one of them must be divisible by 11
	# assume that 'a' is a multiple of 11
	largest = 0
	for b in xrange(999, 99, -1):
		for a in xrange(990, 99, -11):
			tmp_ans = a*b
			if is_palindrome(tmp_ans) and tmp_ans > largest:
				largest = tmp_ans
	print largest


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

def p8():
	'''Solution to problem 8
	'''
	n = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

	largest = product = int(n[0])*int(n[1])*int(n[2])*int(n[3])*int(n[4])

	s = time.time()
	for i in xrange(5, 1000):
		product = int(n[i])*int(n[i-1])*int(n[i-2])*int(n[i-3])*int(n[i-4])
		if product == 0:
			continue
		elif product > largest:
			largest = product
	e = time.time()
	print largest, str(e-s)

def p9():
    '''Solution to problem 9
    '''

    return

def p10(limit=2000000):
    '''Solution to problem 10
    '''

    p, s = 5, 5
    t1 = time.time()
    while p < limit:
	if prime(p):
		s += p
	if prime(p+2):
		s += (p+2)
	p += 6	
    t2 = time.time()
    print s, str(t2-t1)

def main():
	
    func_list = {
        'sieve': sieve,	
    	'if': int_factorization,	
    	'p1': p1, 
    	'p2': p2, 
    	'p3': p3, 
    	'p4': p4, 
    	'p5': p5, 
    	'p6': p6, 
    	'p7': p7,
    	'p7alt': p7_alt,
    	'p8': p8,
    	'p9': p9,
    	'p10': p10
    }
		    
    if len(sys.argv) != 2: 
	print 'Usage: python euler.py <p#>'
    elif not func_list.has_key(sys.argv[1]):
	print 'No solution to', sys.argv[1]
    else:
	func_list[sys.argv[1]]()	

if __name__ == '__main__':
    main()
