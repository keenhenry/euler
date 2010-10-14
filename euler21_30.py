#!/usr/bin/python

""" Project Euler Solutions: Problem 21 - 30
"""

import sys
import time
import euler11_20
import euler1_10
import string
#import math

# function to generate fibonacci numbers: a generator	
def fib():
    a, b, i = 0, 1, 1
    while True:
	yield b, i
	a, b, i = b, a+b, i+1


def p21(limit=10000):
    '''Solution to problem 21 
    '''

    def d(n):
	'''d(n)
	Calculate the sum of proper divisors of n.
	'''
	
	s = 1
	facs = euler11_20.factorize(n)
	for k in facs: s *= (k**(facs[k]+1) - 1)/(k-1)
	return s - n
    
    amicables = [True for x in xrange(limit)]

    # prime numbers cannot be amicable numbers
    # so we eliminate checking those numbers
    for x in euler1_10.sieve(limit):
	amicables[x] = False
   
    # cross out non-amicable numbers
    for x in xrange(220, limit):
	if amicables[x]:
	    y = d(x)
	    amicables[x] = False if (d(y) != x or x == y) else True

    # calculate the sum of amicable pairs and output
    s = 0
    for i in xrange(220, limit): 
	if amicables[i]: s += i
    print s


def p22():
    '''Solution to problem 22 
    '''
    
    f = open('names.txt', 'r')
    names = sorted([n.strip('"') for n in f.read().split(',')])
    f.close()

    # calculate total name scores
    total, base = 0, ord('A')-1
    for i in xrange(len(names)):
	total += (i+1)*sum([ord(c)-base for c in names[i]])
    print total


def p25():
    '''Solution to problem 25 
    '''
    
    for fn, i in fib():
	if len(str(fn)) >= 1000:
	    print i
	    break

def p28(n=1001):
    '''Solution to problem 28 
    '''
    s = 0
    for i in xrange(1, 501):
	s += 4*(4*i*i + i + 1)
    print (s+1)
    

def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
	'p21': p21, 'p22': p22, 'p25': p25, 
	'p28': p28    
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
