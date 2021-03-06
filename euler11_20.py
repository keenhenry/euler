#!/usr/bin/python

""" Project Euler Solutions: Problem 11 - 20
"""

import sys
import time

def factorize(n):
    '''A function that implements integer factorization.
   
    ---Key Arguments---
    @n: number to factorize
    @return: dict that stores the result of factorization
    
    '''

    # initial prime factor
    pf = 2

    # a dictionary of prime factors -> 
    # {k: v} = {prime factor: frequency}
    pfs = {}

    # find the prime factors of a number
    while n != 1:
	if n % pf == 0:	# n has prime factor pf
	    n /= pf		
	    pfs[pf] = (pfs[pf]+1) if pfs.has_key(pf) else 1
	else: 		# n has no prime factor pf; 
			# update pf to find new prime factor
	    pf += 1 if (pf < 3) else 2
    
    return pfs
	

def p11():
    '''Solution to problem 11
    '''
    
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
	    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
	    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
	    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
	    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
	    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
	    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
	    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
	    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
	    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
	    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
	    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
	    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
	    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
	    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
	    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
	    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
	    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
	    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
	    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

    m = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid)-3):
  	    t1 = tuple([grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3]])	# left-right
	    t2 = tuple([grid[j][i], grid[j+1][i], grid[j+2][i], grid[j+3][i]])	# up-down
	    m = max(m, reduce(lambda x, y: x*y, t1), reduce(lambda x, y: x*y, t2))
    
    for i in xrange(len(grid)-3):
	for j in xrange(len(grid)-3):
   	    t3 = tuple([grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]])	# upper left to bottom right
  	    t4 = tuple([grid[j][i+3], grid[j+1][i+2], grid[j+2][i+1], grid[j+3][i]])	# upper right to bottom left
	    m = max(m, reduce(lambda x, y: x*y, t3), reduce(lambda x, y: x*y, t4))
  
    # output answer
    print m


def p12(n_of_divs=500):
    '''Solution to problem 12 
    '''
    
    def tri_gen():
	i = 10
	while True:
	    yield i*(i+1)/2
	    i += 1
   
    def n_of_facs(facs):
	n = 1
	for v in facs.itervalues():
	    n *= (v+1)
	return n

    for tri in tri_gen():
	if n_of_facs(factorize(tri)) >= n_of_divs:
	    print tri
	    break


def p13():
    '''Solution to problem 13 
    '''

    nums = open('bignum', 'r')
    print str(sum([long(line.strip('\n')) for line in nums.readlines()]))[:10]


def p14(uppbound=1000000):
    '''Solution to problem 14 
    '''
  
    # lsn: longest sequence starting number
    lsn, max_seq_len = 2, 2
    seq_table = {1:1}

    # update longest sequence starting number and length
    for start in xrange(2, uppbound):
        cur, count = start, 0
	while cur not in seq_table:
	    cur = (cur/2) if (cur%2==0) else (3*cur+1)
	    count += 1
	
	count += seq_table[cur]
	seq_table[start] = count
   	
	if count > max_seq_len:
	    max_seq_len = count
	    lsn = start

    print 'longest seqence staring number:', \
		lsn, "length:", max_seq_len


def p15(n=20):
    '''Solution to problem 15 
    '''
    
    # initialize grid using list comprehension
    grid = [[1 if j==0 or i==0 else 0 for j in xrange(n+1)] for i in xrange(n+1)]
    
    # calculating routes
    for i in xrange(1, 21):
	for j in xrange(1, 21):
	    grid[i][j] = grid[i-1][j] + grid[i][j-1]

    # output answer: grid[n][n]
    print grid[n][n]


def p16(n=2**1000):
    '''Solution to problem 16
    This solution outputs the answer in less than 0.0006 second!
    And it is a one liner!!! This is really good python!
    '''
    print sum(map(int, list(str(n))))


def p17():
    '''Solution to problem 17
    '''

    translate = {
    	'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
	'6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
	'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
	'16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
	'30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
	'80': 'eighty', '90': 'ninety', '100': 'onehundred', '200': 'twohundred', '300': 'threehundred', 
	'400': 'fourhundred', '500': 'fivehundred', '600': 'sixhundred', '700': 'sevenhundred', '800': 'eighthundred', 
	'900': 'ninehundred', '1000': 'onethousand'
    }

    def two_digits(n):
	str_n = str(n)
	
	if n%10 == 0:
	    return translate[str_n]
	if n <= 20:
	    return translate[str_n]
	if n < 30:
	    return translate['20'] + translate[str_n[1]]
	if n < 40:
	    return translate['30'] + translate[str_n[1]]
	if n < 50:
	    return translate['40'] + translate[str_n[1]]
	if n < 60:
	    return translate['50'] + translate[str_n[1]]
	if n < 70:
	    return translate['60'] + translate[str_n[1]]
	if n < 80:
	    return translate['70'] + translate[str_n[1]]
	if n < 90:
	    return translate['80'] + translate[str_n[1]]
	if n < 100:
	    return translate['90'] + translate[str_n[1]]
    
    def three_digits(n):
	if n%100 == 0:
	    return translate[str(n)]
	if n < 200:
 	    return translate['100'] + 'and' + two_digits(n-100)
	if n < 300:
 	    return translate['200'] + 'and' + two_digits(n-200)
	if n < 400:
 	    return translate['300'] + 'and' + two_digits(n-300)
	if n < 500:
 	    return translate['400'] + 'and' + two_digits(n-400)
	if n < 600:
 	    return translate['500'] + 'and' + two_digits(n-500)
	if n < 700:
 	    return translate['600'] + 'and' + two_digits(n-600)
	if n < 800:
 	    return translate['700'] + 'and' + two_digits(n-700)
	if n < 900:
 	    return translate['800'] + 'and' + two_digits(n-800)
	if n < 1000:
 	    return translate['900'] + 'and' + two_digits(n-900)

    s = ''
    for i in xrange(1, 1001):
	if i < 100:
            s += two_digits(i)
    	elif i < 1000:
            s += three_digits(i)
    	else:
            s += translate[str(i)]
    
    print len(s)


def p19():
    '''Solution to problem 19
    '''

    def days_of_month(m, y):
	if m==2:
	    return 29 if (y%4 == 0 and y%100 != 0 or y%400 == 0) else 28
    	else:
	    return 30 if (m==4 or m==6 or m==9 or m==11) else 31
	
    first_sun, suns = 6, 0
    for y in xrange(1901, 2001):
	for m in xrange(1, 13):
	    if first_sun == 1: suns += 1
	    m_days = days_of_month(m, y)
	    while first_sun <= m_days: first_sun += 7
	    first_sun -= m_days
    print suns


def p20(n=100):
    '''Solution to problem 20
    Again it is a one liner!!! This is really good python!
    '''

    #n_fac = reduce(lambda x,y: x*y, xrange(1,n))
    print sum(map(int, list(str(reduce(lambda x,y: x*y, xrange(1,n))))))


def main():
    '''Main program of module euler11_20 
    '''

    func_list = {
        'p11': p11, 'p12': p12, 'p13': p13, 'p14': p14, 'p15': p15,    
	'p16': p16, 'p17': p17, 'p19': p19, 'p20': p20 
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
