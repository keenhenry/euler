#!/usr/bin/python

""" Project Euler Solutions: Problem 41 - 50
"""

import sys
import time
#import math

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

def p48(n=1000):
    '''Solution to problem 48
    '''

    print str(sum(map(lambda x: x**x, range(1, n+1))))[-10:]
    
def main():
    '''Main program of module euler21_30 
    '''

    func_list = {
        'p42': p42, 'p48': p48
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
