#!/usr/bin/python 

""" Project Euler Solutions: Problem 31 - 40 
""" 

import sys
import time
from euler1_10 import sieve


def fib():
    '''A function to generate fibonacci numbers: a generator	
    '''
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

def dec2bin(n):
    '''A function to convert an integer from decimal to binary representation (string)

    There are 1000 ways to do this. Here I am just showing one of it.
    '''
    
    s = ""
    
    while n: 
        s = "1" + s if (n & 1) else "0" + s
        n = (n >> 1)
    return s

def is_palindrome(n):
    '''A function to check palindrome.
    '''
    
    s = str(n) if not isinstance(n, str) else n 
    return s[::-1] == s

def factorial(n):
    '''A function to calculate the factorial of n.
    '''

    ans = 1
    for i in xrange(1, n+1): ans *= i
    return ans	

def gcd(a, b):
    '''A function to find the greatest common advisor of two integers
    '''

    if a == 0:
        return b;

    while b != 0:
        if a > b: a = a - b
        else    : b = b - a

    return a

def permute(prefix="", rest="", fn=None):
    '''This is a function to list the permutaions of a string IN ORDER

    @prefix: the prefix of the string to be permuted
    @rest: the rest of the string to be permuted
    @fn: a function passed in to operate on the permuted string
    '''

    l = len(rest)

    if l == 0:
        fn(prefix)
    else:
        for i in xrange(0, l):
            permute(prefix+rest[i], rest[0:i]+rest[i+1:l], fn)


def p31():
    '''Solution to problem 31 

    1a + 2b + 5c + 10d + 20e + 50f + 100g + 200h = 200
    
    This problem is a typical form of dynamic programming:

    Let final solution set be C(N, S) -- a function of N and S.
    Let N = The target currency -- 200 in this problem.
    Let S = a set of available denomination for change -- {1, 2, 5, 10, 20, 50, 100, 200} in this problem.
    Let m = the index of the largest demomination in S.

    The formula: C(N, S) = C(N-Sm, S) + C(N, S-Sm)

    We can use recursive algorithm to solve this problem ... OR using dynamic programming!
    Watch out for boundary conditions though.
    '''
    
    target, coins = 200, [1, 2, 5, 10, 20, 50, 100, 200]
    # target, coins = 100, [i for i in xrange(101)] ===> for Problem 76
    
    #
    # Recursive solution (about 3 seconds):
    #

    #def ways(N=0, S=[]):
    	# 3 base conditions
    #	if N==0: return 1
    #	if N<0 or (N>=1 and len(S)==0): return 0
	
    #	return ways(N,S[:-1]) + ways(N-S[-1], S)
    
    #print ways(target, coins)
    
    #
    # Dynamic programming solution (within 1 second):
    #

    #ways = [1]+[0]*target	# an intial table
    #for coin in coins:
    #	for i in range(coin, target+1):
    #   	    ways[i] += ways[i-coin]
    #print ways[target]
    ways = [([1]+[0]*target) for i in xrange(len(coins)+1)]
    for m in xrange(1, len(coins)+1):
    	for n in xrange(1, target+1):
	    ways[m][n] = ways[m][n-coins[m-1]] + ways[m-1][n]
    print ways[len(coins)][target]
    #print ways[len(coins)][target] - 1 # for problem 76

    #
    # Brute-force ... not pretty ... but worked (in about 11 seconds)!
    #

    #ways = 0
    #for a in xrange(0, 201):
    #  for b in xrange(0, 101):
    #    if a+2*b > 200: break
    #    for c in xrange(0, 41):
    #	  if a+b*2+c*5 > 200: break
    #	  for d in xrange(0, 21):
    #	    if a+b*2+c*5+d*10> 200: break
    #	    for e in xrange(0, 11):
    #	      if a+b*2+c*5+d*10+e*20 > 200:break
    #	      for f in xrange(0, 5):
    #		if a+b*2+c*5+d*10+e*20+f*50 > 200:break
    #	        for g in xrange(0, 3):
    #		  if a+b*2+c*5+d*10+e*20+f*50+g*100 > 200:break
    #		  for h in xrange(0, 2):
    #		    if (a+2*b+5*c+10*d+20*e+50*f+100*g+200*h == 200): ways += 1
    #print ways

def p32():
    '''Solution to problem 32

    Obviously, this is not an optimal way to solve this problem...
    This is brute-forceing in about ~5 seconds!
    '''

    answers = set()
    def wrapper_func(arg):
        '''A wrapper function to be passed to permute.

        This function takes only one argument, because in 'permute', 
        it is called with only one argument. However, to make it more general,
        you can declare it to be 'wrapper_func(*args), which will take a list
        of arguments.
        '''

        # print arg
        multiplicand1 = int(arg[0])
        multiplier1   = int(arg[1:5])

        multiplicand2 = int(arg[0:2])
        multiplier2   = int(arg[2:5])

        product       = int(arg[5:])

        if multiplicand1*multiplier1 == product:
            if product not in answers:  answers.add(product) #[product] = (multiplicand1, multiplier1)
        elif multiplicand2*multiplier2 == product:
            if product not in answers:  answers.add(product) #[product] = (multiplicand2, multiplier2)

    permute("", "123456789", wrapper_func)
    print sum(answers)

def p33():
    '''Solution to problem 33 

    This problem can be easily brute-forced. 

    However, we can eliminate some unnecessary computation by further
    tightening the loops.
    '''
    
    fractions = []
    product_of_numerators, product_of_denominators = 1, 1
    for tens in xrange(9, 0, -1):
        for units in xrange(9, 0, -1):
            for numerator_tens in xrange(tens-1, 0, -1):
                numerator   = numerator_tens*10 + tens
                denominator = tens*10 + units 

                if (numerator / float(denominator)) == (numerator_tens / float(units)):
                    fractions.append(str(numerator) + '/' + str(denominator))
                    product_of_numerators   *= numerator
                    product_of_denominators *= denominator

    ans = product_of_denominators / (gcd(product_of_denominators, product_of_numerators))
    print 'The four fractions are: ', fractions, 'And the final answer is: ', ans 
   

def p34(upper=2540160):
    '''Solution to problem 34 
    
    This problem is similar to problem 30. The key is to find the upper bound.
    upper==2540160==7x9!
    '''
   
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    s = 0    # sum of all numbers which are equal to the sum of factorial of their digits.
    for i in xrange(100, upper):
    	sum_of_factorial_of_digits = 0
	for d in ydigits(i): sum_of_factorial_of_digits += facts[d]
    	if i == sum_of_factorial_of_digits: s += i
    print s

def p35(limit=1000000):
    '''Solution to problem 35 
    '''
   
    # Building a dictionary of primes below 1 million
    primes = {}
    for p in sieve(1000000):
    	primes[p] = False	# Initialize to NOT a circular prime
    
    n_of_cprimes = 0    # number of circular primes
    for p in primes.keys():
	n = str(p)
	l = len(n)	# number of iterations to rotate the string
	while l != 0:
	    n = n[1:] + n[0]	# string rotation
	    if int(n) not in primes: break
	    l -= 1
	if l == 0: 
	    n_of_cprimes += 1
	    primes[p] = True
    print n_of_cprimes

def p36(limit=1000000):
    '''Solution to problem 36 
    '''
    
    s = 0    # the sum of all numbers which are palindrom in base10 and base2
    for i in xrange(1, limit, 2):    # only ODD numbers can be candidates!	
        if is_palindrome(i) and is_palindrome(bin(i)[2:]): s += i
        #if is_palindrome(i) and is_palindrome(dec2bin(i)): s += i
    print s

def p37():
    '''Solution to problem 37
    '''
  
    def is_truncatable_prime(p=0, d=None):
	"Return True if p is a truncatable prime from left to right, otherwise False"

	rel, p_from_right, p_from_left = True, str(p), str(p)
	l = len(p_from_left)

	while l > 0:
	    if int(p_from_left) in d and int(p_from_right) in d: 
	    	p_from_left = p_from_left[1:]
		p_from_right = p_from_right[:-1]
		l -= 1
	    else: 
	    	rel = False
		break
	return rel

    s, primes = 0, set([p for p in sieve(800000)])
    for p in xrange(23, 800000, 2): 
    	if is_truncatable_prime(p, primes): s += p
    print s

def p38():
    '''Solution to problem 38

    1. Permute pandigital number string from "987654321" to "918273645" (biggest mentioned in the problem)
    2. Test if that permuted number can be decomposed into [X*1][X*2][X*3]...[X*n] form
    '''
  
    def print_concat_product(x):
        # the base of the concatenated product could be a (1-digit, but 1-digit example is mentioned in the problem i.e. 9 with (1,2,3,4,5)) 
        # 2-digit, 3-digit, or 4-digit (and no more) number 
        for i in xrange(2, 5):
            concat_product = x[0:i]
            n, base = 2, int(concat_product)
            while len(concat_product) <= 9:
                concat_product += str(base*n)
                if len(concat_product) == 9 and concat_product == x:
                    print x, "and its base:", str(base)
                    break
                n += 1

    # print out all pandigital 9-digit numbers whose first digit is 9
    # in the order of permutation, which is from biggest to smallest
    permute("9", "87654321", print_concat_product)

def p39():
    '''Solution to problem 39 
    '''

    # The key question is how to generate Pythagorean triples
    # Use this formula: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
    # where m and n are coprime and (m - n) is odd, to generate
    # PRIMITIVE triples. 
    # This formula is guaranteed to generate ALL primitive triples
    # if the conditions for m, n are satisfied.
    #
    # After you get all primitives primes, you can use them to
    # find non-primitive ones easily.
    #
    # Other properties you might take into account:
    # 1) sum of pythagorean triple is always an even number
    # 2) Let m's always be greater than n's for ease of computation 

    # initialize dictionary p: a dictionary storing (perimeter, count) pairs
    s = time.time()
    p = {} 
    n = 1
    while n <= 15:
        m = n+1
        while True:
            if gcd(m, n) == 1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n

                if (a+b+c) <= 1000:
                    # a primitive pythagorean triple
                    if (a+b+c) in p: p[a+b+c] += 1                       
                    else           : p[a+b+c] = 1

                    # count the non-primitive pythagorean triples
                    for i in xrange(2*(a+b+c), 1001, a+b+c): 
                        if i not in p: p[i] = 1                       
                        else         : p[i] += 1
                else:
                    break
            m += 2
        n += 1

    # return answer: the maximized key value of p
    ans = max(p, key=p.get)
    e = time.time()
    print ans, ' finished in ', str(e - s), ' seconds'


def p40():
    '''Solution to problem 40 
    '''
    
    ans, s, n = 1, '0', 1
    while len(s) < 10000001:
    	s += str(n)
	n += 1
    ans = int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])  
    print ans

def main():
    '''Main program of module euler31_40 
    '''

    func_list = {
            'p31': p31, 'p32': p32, 'p33': p33, 'p34': p34, 'p35': p35, 
            'p36': p36, 'p37': p37, 'p38': p38, 'p39': p39, 'p40': p40 
    }
		    
    if func_list.has_key(sys.argv[1]):
        func_list[sys.argv[1]]()	
    else:
        print 'No solution to', sys.argv[1]
