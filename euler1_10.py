#!/usr/bin/python

""" Project Euler Solutions
"""

import sys
import time
import math

def prime(n):
    '''Primality testing function

    --key Arguments--
    @n: number to test primality
    @return: boolean

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
    p = 7					# p = 6k+1
    while p**2 <= n:
	if n%p==0:		return False
	if (p+4)**2 > n:	return True
	if n%(p+4)==0:		return False	# p = 6k+5 or 6k-1
	p += 6		
	
    return True	


def factorize(n=600851475143):
    '''A function that implements integer factorization.
    This function is suitable for use with numbers that are not too big,
    that is, less than 2^50. The bigger the number, the slower this algo
    runs.
    
    --Key Arguments--
    @n: number to factorize
    @return:

    '''

    # make a copy of n
    composite = n

    # initial prime factor
    pf = 2

    # a dictionary of prime factors -> {k: v} = {prime factor: frequency}
    pfs = {}

    # find the prime factors of a number
    while n != 1:
	if n % pf == 0:	# n has prime factor pf
	    n /= pf		
	    pfs[pf] = (pfs[pf]+1) if pfs.has_key(pf) else 1
	else: 		# n has no prime factor pf; update pf to find new prime factor
	    pf += 1 if (pf < 3) else 2
	
    # output result
    primes = sorted(pfs.keys())

    ans = str(composite) + ' = '
    for p in primes:
	ans += str(p)+'^'+str(pfs.get(p)) if pfs[p] > 1 else str(p)  # 'p^n' or 'p'
	ans += '' if p==primes[-1] else ' X '			   
    print ans


def sieve(upper=1000):
    '''The Sieve of Eratosthenes algorithm
    
    --Key Arguments--
    @upper: the upper bound of prime number list
    @return: a list of prime numbers
    
    '''

    # creating an array to hold boolean values
    nums = [False, False]
    for i in xrange(2, upper):
        nums.append(True)

    # crossing out composite numbers
    for i in xrange(2, int(math.sqrt(upper))+1):
    	if nums[i]:
	    j = i*i
	    while j < upper:
		nums[j] = False
		j += i

    # return a list of primes using generator
    for i in xrange(2, upper):
	    if nums[i]: yield i


def p1():
    '''Solution to problem 1
    '''

    print (sum(range(0, 1000, 3))+sum(range(0, 1000, 5))-sum(range(0, 1000, 15)))


def p2(maxlimit=4000000):
    '''Solution to problem 2
    
    --key Arguments--
    @maxlimit: upper bound for fibonacci numbers
    @return:

    '''

    # function to generate fibonacci numbers: a generator	
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
    
    --key Arguments--
    @n: number to factorize
    @return:
    
    '''

    # initial largest prime factor (lpf)
    lpf = pf = 2

    # the main algorithm to find the largest prime factor of a number
    while n != 1:
	if n % pf == 0:
	    n /= pf
	    lpf = pf
	else:
	    pf += 1 if pf < 3 else 2

    # output answer:
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

    for i in xrange(5, len(n)):
	product = int(n[i])*int(n[i-1])*int(n[i-2])*int(n[i-3])*int(n[i-4])
	if product == 0:
		continue
	elif product > largest:
		largest = product
    print largest


def p9():
    '''Solution to problem 9
    let a = m^2 - n^2
    let b = 2*m*n
    let c = m^2 + n^2
    a + b + c = 1000 ==> m(m+n) = 500
    assume m > n, then m = 20, n =5
    => a = 375, b = 200, c = 425
    a*b*c = 31875000

    '''

    print 31875000


def p10(limit=2000000):
    '''Solution to problem 10
    This solution uses sieve() generator to generate prime numbers.
    Then iterator through those numbers generated to find the sum.
    This function obtains the answer within 1.5 seconds.
    
    --Key Arguments--
    @limit: the upper bound of prime numbers
    @return: 
    
    '''
   
    s = 0
    for p in sieve(limit):
	s += p
    print s


def main():
    '''Main program of module euler1_10 
    '''

    func_list = {
    	'factor': factorize, 'p7alt': p7_alt,
    	'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'p5': p5,     	
	'p6': p6, 'p7': p7, 'p8': p8, 'p9': p9,	'p10': p10
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
