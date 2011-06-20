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

def ydigits(num=0):
    '''A function to extract the digits of an integer.
    '''

    while num!=0:
    	d, num = num%10, num/10
	yield d

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

def p24(p='0123456789'):
    '''Solution to problem 24

    I solved it by hand! Not that hard to do it!
    '''
    
    print '2783915460'

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
    
def p29():
    '''Solution to problem 29

    Let's try brute force method first.
    '''
    
    nums = {}
    for i in xrange(2, 101):
	for j in xrange(2, 101):
	    num = i**j
	    if num not in nums: nums[num] = True
    print len(nums)

def p30(upper_bound=354294):
    '''Solution to problem 30

    This solution is brute force. However, the tricky part is to determine
    the upper bound for the search (How do you prove that it is the absolute upper bound?).
    The upper bound used in this solution is just a simple guess (6 * 9^5 = 354294).
    '''

    s = 0   # set initial sum to zero

    # the lower bound of the loop is also tricky, 
    # in this solution, this is also a guess, but it's a guess that makes sense.
    for i in xrange(upper_bound, 1000, -1):
	sum_of_5th_power_of_digits = 0
    	for j in ydigits(i):
	    sum_of_5th_power_of_digits += j**5
	if i == sum_of_5th_power_of_digits:
	    #print i
	    s += i
    print s
    
    # A one-liner solution reference:
    # print sum([n for n in xrange(1000,354294) if sum(int(i)**5 for i in str(n)) == n])

def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
	'p21': p21, 'p22': p22, 'p24': p24, 'p25': p25, 
	'p28': p28, 'p29': p29, 'p30': p30    
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
