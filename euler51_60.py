#!/usr/bin/python

""" Project Euler Solutions: Problem 51 - 60
"""

import sys
import time
import euler31_40

def p52():
    '''Solution to problem 52

    In this problem, I used brute force to break it. It runs within a second.
    However, this problem can be solved trivially by knowing that 1/7 has that 
    cicular property.
    '''
  
    def circular(n=125874):
    	"Test if n is circular within 2x, 3x, 4x, 5x, 6x mutitples"

    	ans, digits = True, set(str(n))	   # a set of digits of original number
	for i in xrange(2, 7):
	    t = n * i
	    t_digits = set(str(t))
	    if t_digits != digits: 
	    	ans = False
		break
	return ans

    x, not_found = 101, True
    while not_found:
    	if len(str(x))==len(str(6*x)) and circular(x): not_found = False
	else: x += 1
    print x

def p53():
    '''Solution to problem 53

    This problem can be solved by calculating Pascal's triangle.
    And remember to use dynamic programming techniques.
    
    You don't need to build the whole triangle, you only need half
    of it.
    '''
  
    count = 2
    pascal_triangle_row = [0 if i <= 37 or i == 50 else
                            (euler31_40.factorial(23)/(euler31_40.factorial(i-38)*euler31_40.factorial(61-i))) for i in xrange(0, 51)]

    for n in xrange(23, 100):
        if n%2 == 1:
            for i in xrange(50, 49-(n+1)/2, -1):
                if i == 50: 
                    pascal_triangle_row[i] = pascal_triangle_row[i-1] * 2
                    if pascal_triangle_row[i] > 1000000L: count += 1
                else:
                    pascal_triangle_row[i] = pascal_triangle_row[i] + pascal_triangle_row[i-1]
                    if pascal_triangle_row[i] > 1000000L: count += 2
        else:
            for i in xrange(49-(n+1)/2, 50):
                pascal_triangle_row[i] = pascal_triangle_row[i] + pascal_triangle_row[i+1]
                if pascal_triangle_row[i] > 1000000L: count += 2
    print count

def p55(ulimit=10000):
    '''Solution to problem 55
    '''
  
    # initially, assume every number below 10000 is lychrel 
    num_lychrel = ulimit - 1
    for i in xrange(1, ulimit):
        cur, num_iter = i, 0

        while num_iter < 50:
            nxt = cur + int(str(cur)[::-1])
            if euler31_40.is_palindrome(nxt):
                # this number is not a lychrel, because a palindrome is found
                # through the reverse-add process; therefore 
                # decrease the number of lychrel numbers by 1!
                num_lychrel -= 1
                break
            else:
                cur = nxt
                num_iter += 1

    print num_lychrel

def p56():
    '''Solution to problem 56

    Brute-force within 1 second!
    '''
  
    ans = 0
    for a in xrange(2, 100):
        for b in xrange(80, 100):
            ans = max(ans, sum(map(int, str(a**b))))
    print ans

def main():
    '''Main program of module euler51_60 
    '''

    func_list = {
            'p52': p52, 'p53': p53, 'p55': p55, 'p56': p56
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
