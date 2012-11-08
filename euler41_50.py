#!/usr/bin/python

""" Project Euler Solutions: Problem 41 - 50
"""

import sys
import time
from heapq import *
from euler1_10 import prime
from euler1_10 import sieve
from euler11_20 import factorize

def p41():
    '''Solution to problem 41

    1. Generate pandigital numbers (generate permutation by BFS)
    2. Test if it is a prime using a function implemented in euler1_10

    Note: 
    - only 7-digit and 4-digit permutations are possible to generate primes
    - Therefore, try 7-digit permutation first!
    - only need to find the biggest prime pandigital number
    - is there a neater solution? for example, can you avoid some unnecessary calculations in the recursion?
    '''

    forbidden = set([2,4,5,6]) 
    def bfs(digits, depth, n):
        if depth == 1:
            n += digits[0]
            return n if (digits[0] not in forbidden) and prime(n) else -1
        else:
            biggest, orig_n = 0, n
            for d in digits:
                n = orig_n + d*(10**(depth-1))

                # create a copy of parent's digit list
                digits_left = digits[:]
                digits_left.remove(d)

                # search deeper for answer
                biggest = max(biggest, bfs(digits_left, depth-1, n))
            return biggest

    print bfs([7, 6, 5, 4, 3, 2, 1], 7, 0)

def p42():
    '''Solution to problem 42
    '''
    
    with open('words.txt', 'r') as f:
    	words = f.read()
   
    def get_word_value(word=''):
    	if word=='': return 0
	return sum(map(lambda c: ord(c)-ord('A')+1, word))

    word_list = map(lambda s: s[1:-1], words.split(','))
    n_of_trinums, Tn = 0, set([0.5*i*(i+1) for i in xrange(1, 1000)])
    for word in word_list:
    	if get_word_value(word) in Tn: n_of_trinums += 1
    print n_of_trinums

def p45():
    '''Solution to problem 45
    '''

    # All the triangle numbers are Hexagonal numbers except '3'!
    #Tn = set([0.5*i*(i+1) for i in xrange(286, 100000)]) 
    Pn = set([0.5*i*(3*i-1) for i in xrange(166, 40000)]) 
    Hn = set([i*(2*i-1) for i in xrange(144, 30000)])
    R = Pn & Hn
    for n in R: print n

def p47():
    '''Solution to problem 47
    '''

    i = 2*3*5*7 
    while True:
        if len(factorize(i))==4 and len(factorize(i+1))==4 and len(factorize(i+2))==4 and len(factorize(i+3))==4:
            break
        else:
            i += 1
    print i


def p48(n=1000):
    '''Solution to problem 48
    '''

    print str(sum(map(lambda x: x**x, range(1, n+1))))[-10:]
    
def p50(n=1000000):
    '''Solution to problem 50

    This solution can be executed within a second
    '''

    # first generate a set of primes below n for testing primality in O(1)
    primes = set([p for p in sieve(n)])

    # create a list of consective primes that add up just below n
    cps, s = [], 0
    for p in sieve(n):
        if s <= n: 
            s += p
            cps.append(p)
        else:      
            break

    # let's search the answer!
    ans, b, e, found = 0, 0, 0, False
    for l in xrange(len(cps), 0, -1):
        for i in xrange(0, len(cps)-l+1):
            s = sum(cps[i:i+l])

            # the first sum found is actually the answer! 
            # no needs to continue searching anymore!
            if s in primes: 
                ans, b, e, found = s, i, i+l, True
                break

        if found: break

    print ans, 'with', len(cps[b:e]), 'terms'
    # print cps[b:e]


def main():
    '''Main program of module euler41_50 
    '''

    func_list = {
            'p41': p41, 'p42': p42, 'p45': p45, 
            'p47': p47, 'p48': p48, 'p50': p50
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
