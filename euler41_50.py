#!/usr/bin/python

""" Project Euler Solutions: Problem 41 - 50
"""

import sys
import time
from heapq import *
from euler1_10 import prime

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

def p48(n=1000):
    '''Solution to problem 48
    '''

    print str(sum(map(lambda x: x**x, range(1, n+1))))[-10:]
    
def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
        'p41': p41, 'p42': p42, 'p45': p45, 'p48': p48
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
