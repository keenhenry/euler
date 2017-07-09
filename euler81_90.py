#!/usr/bin/python

""" Project Euler Solutions: Problem 81 - 90
"""

import sys
import time

def p81():
    '''Solution to problem 81

    This problem can be seen as a shortest path graph problem, and 
    solved by a shortest path algorithm. 

    Each number in the matrix can be seen as a vertex in a graph.
    The shortest path to a vertex can be derived from its neighbors,
    that is, the vertex right above it and the vertex left to it.

    By taking advantages of a 2D matrix data structure, you can easily 
    navigate through the graph with index arithmetics, and store 
    minimal path sums for each vertex in the matrix.

    It is easy to implement this shortest path algorithm, however 
    it is not the most optimal solution.

    Dynamic Programming is your friend in this problem, think about 
    how you can solve it with a DP algorithm?

    This problem is similar to problem 82 and 83!
    '''

    matrix = []

    # load file content into a data structure in memory
    f = open('matrix.txt', 'r')

    for line in f.readlines():
        numbers = line.rstrip().split(',')
        matrix.append([int(number) for number in numbers])

    # calculate minimal path sums
    nr, nc = len(matrix), len(matrix[0])
    for row in xrange(nr):
        for col in xrange(nc):
            if row == 0 and col == 0: continue  # skip source node
            elif row == 0:
                matrix[row][col] += matrix[row][col-1]
            elif col == 0:
                matrix[row][col] += matrix[row-1][col]
            else:
                matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1])

    # the shortest path sum from source vertex (matrix[0][0]) to 
    # the destination vertex (matrix[79][79]) is stored at 
    # matrix[79][79], so we print the answer there
    print matrix[nr-1][nc-1]

def p82():
    '''Solution to problem 82

    This problem can be seen as a shortest path graph problem, and 
    solved by a shortest path algorithm. 

    This problem needs to run shortest path algorithm from several
    sources in the left most column in the matrix. That means you 
    need to run SPA several times!

    This problem is similar to problem 81 and 83!
    '''

    matrix = []

    # load file content into a data structure in memory
    f = open('matrix.txt', 'r')

    for line in f.readlines():
        numbers = line.rstrip().split(',')
        matrix.append([int(number) for number in numbers])

    # calculate minimal path sums
    nr, nc = len(matrix), len(matrix[0])

    # print answer
    print matrix[nr-1][nc-1]

def main():
    '''Main program of module euler51_60 
    '''

    func_list = {
            'p81': p81, 'p82': p82
    }
		    
    if func_list.has_key(sys.argv[1]):
        func_list[sys.argv[1]]()	
    else:
        print 'No solution to', sys.argv[1]
