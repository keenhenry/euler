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

def p54():
    '''Solution to problem 54: Winner of poker hands?
    '''

    # a function to calculate the rank of a hand
    def getRank(v_map, s_map):
        rank = 1

        if len(s_map) == 1: # all cards are in the same suit
            if sum(v_map.keys()) == 60:
                rank = 10   # Royal Flush
            elif len(v_map) == 5 and (max(v_map)-min(v_map)) == 4:
                rank = 9    # Straight Flush
            else:
                rank = 6
        elif len(v_map) == 2: # four of a kind or full house
            numOfAKind = v_map.itervalues().next()
            if numOfAKind == 4 or numOfAKind == 1:
                rank = 8    # Four of a Kind
            else:
                rank = 7    # Full House
        elif len(v_map) == 3:   # Three of a Kind or Two Pairs
            for k in v_map:
                if v_map[k] == 3: 
                    rank = 4
                    break
                if v_map[k] == 2: 
                    rank = 3
                    break
        elif len(v_map) == 4: # One Pair
            rank = 2
        elif (max(v_map)-min(v_map)) == 4: # len(v_map) == 5
            rank = 5        # Straight

        return rank

    def compare_value(v_map1, v_map2):
        # sort value_map first by values then by keys
        sorted_values1 = sorted(v_map1.items(), key=lambda x: (x[1], x[0]), reverse=True)
        sorted_values2 = sorted(v_map2.items(), key=lambda x: (x[1], x[0]), reverse=True)

        for i in xrange(len(sorted_values1)):
            if sorted_values1[i][0] > sorted_values2[i][0]:
                return 1
            elif sorted_values1[i][0] < sorted_values2[i][0]:
                return 0
            # a draw, continue next loop

    # some values for bookkeeping
    num_p1_winner = 0
    convert_value = { '2':  2, '3':  3, '4':  4, '5':  5, '6':  6,
                      '7':  7, '8':  8, '9':  9, 'T': 10, 'J': 11,
                      'Q': 12, 'K': 13, 'A': 14 }

    # use two dict to keep track of suits and values
    value_map1, suit_map1, value_map2, suit_map2 = {}, {}, {}, {}

    f = open('poker.txt', 'r')
    for line in f.readlines():
        ten_cards = line.split()

        # parse cards into data structures
        for i in xrange(10):
            value = convert_value[ten_cards[i][0]]
            if i < 5:
                if value in value_map1: 
                    value_map1[value] += 1
                else:
                    value_map1[value]  = 1

                if ten_cards[i][1] in suit_map1:
                    suit_map1[ten_cards[i][1]] += 1
                else:
                    suit_map1[ten_cards[i][1]] = 1
            else:
                if value in value_map2: 
                    value_map2[value] += 1
                else:
                    value_map2[value] = 1

                if ten_cards[i][1] in suit_map2:
                    suit_map2[ten_cards[i][1]] += 1
                else:
                    suit_map2[ten_cards[i][1]] = 1

        p1_rank = getRank(value_map1, suit_map1) 
        p2_rank = getRank(value_map2, suit_map2)

        if p1_rank > p2_rank:
            num_p1_winner += 1
        elif p1_rank == p2_rank:
            num_p1_winner += compare_value(value_map1, value_map2)

        # refresh dicts
        value_map1.clear()
        suit_map1.clear()
        value_map2.clear()
        suit_map2.clear()

    f.close()
  
    print num_p1_winner

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
            'p52': p52, 'p53': p53, 'p54': p54, 'p55': p55, 'p56': p56
    }
		    
    if func_list.has_key(sys.argv[1]):
	func_list[sys.argv[1]]()	
    else:
	print 'No solution to', sys.argv[1]
