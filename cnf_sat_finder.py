#!/usr/bin/env python

###############################################################################
# cnf_sat_finder.py
#
# CNF-Satisfiable solution finder.
#
# Description:
# Permutes through all the boolean variations from 0 till 2^n
# Plugs in each boolean permutation into the cnf expression 
# until a solution is found.
#
# cnf expressions are represented as a list of tuples 
# containing either of the following 2 lambda functions:
#   negate = lambda b: not b
#   identify = lambda b: b
# 
# These cnf expressions are randomly generated in to which the boolean 
# permutations are plugged into to evaluate its truthiness.
#
############################################################################### 
# 
# 
# Usage: 
#   cnf_sat_finder.py <cnf size> <number of cnf tuples>
#
# Example:
#   [ramin@laptop py_projects]$ ./cnf_sat_finder.py 3 3
#   Generated CNF Expression:
#       (identify(X) or identify(X) or identify(X)) and
#       (identify(X) or negate(X) or identify(X)) and
#       (identify(X) or negate(X) or identify(X))
#   Solution:
#       (identify(False) or identify(False) or identify(True)) and
#       (identify(False) or negate(False) or identify(False)) and
#       (identify(False) or negate(False) or identify(False))
#   Solution took 0.00402617454529 sec to compute running 64 iterations
#   Architecture run on: 
#   Linux laptop 2.6.29-ARCH #1 SMP PREEMPT Tue Apr 7 12:47:56 UTC 2009 i686
#   
#
#
#
# Author:
# Ramin Rakhamimov
# ramin32@gmail.com
# http://raminrakhamimov.tk
#################################################################################

import sys
import random
import time
import math
import itertools
#import os

"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

def for_loop(start, end):
    """loop for long values."""
    while start < end:
        yield start
        start += 1

def generate_cnf_tuple(cnf_size):
    """Generates a cnf list."""
    operators = (negate, identify)
    return [random.choice(operators) for i in xrange(cnf_size)]

def generate_random_cnf_expression(cnf_size, expression_size):
    """Creates a list of cnf lists of given size."""
    return [generate_cnf_tuple(cnf_size) for i in xrange(expression_size)]

def create_boolean_groups(x, max_size, cnf_size):
    """Constructs binary groups of the cnf size taken from splitting 
    the binary string representation of x."""

    # strip the 0b hex header and pad with 0's
    raw_binary = bin(x)[2:].zfill(max_size)                   
    # map 0's and 1's to booleans
    booleans = [{'0': False, '1':True}[b] for b in raw_binary] 
    # split booleans list into tuples of cnf size
    binary_groups = group_split(booleans, cnf_size)            
    return binary_groups

def group_split(seq, size):
    """Splits the given sequence into groups of size."""
    return [seq[i:i+size] for i in xrange(0, len(seq), size)]


def evaluate_cnf_with_booleans(cnf_exp, boolean_groups):
    """Plugs in the binary string into the cnf expression 
    evaluating to true or false."""
    return all(any(f(b) for f,b in itertools.izip(cnf,booleans)) 
               for cnf, booleans in itertools.izip(cnf_exp, boolean_groups))

def solve_cnf(cnf_exp, cnf_size):
    """Returns first cnf-sat match using bruteforce."""
    size = len(cnf_exp) * cnf_size
    iterations = 0
    for i in for_loop(0, 2**size):
        boolean_groups = create_boolean_groups(i, size, cnf_size)
        if evaluate_cnf_with_booleans(cnf_exp, boolean_groups):
            return boolean_groups, iterations
        iterations += 1
    return None, iterations


def operator_str(operator, param='X'):
    """Returns a pretty string of the function."""
    if operator == identify:
       return 'identify(%s)' % param 
    elif operator == negate:
        return 'negate(%s)' % param 

    raise ValueError('input %s not negate or identify' % str(operator))

def create_cnf_string(cnf, booleans):
    if booleans == None:
        booleans = itertools.repeat('X')
    return " or ".join(operator_str(op, param) for op, param in  itertools.izip(cnf, booleans))

def parentecize(inner_part):
    return "".join(('(',inner_part ,')'))

def cnfize(cnf, booleans):
    return parentecize(create_cnf_string(cnf, booleans))

def pretty_print(cnf_exp, solution=itertools.repeat(None)):
    print '\t' + " and\n\t".join( cnfize(cnf, booleans) for cnf, booleans in itertools.izip(cnf_exp, solution))
    
def main():
    random.seed(time.time())
    try:
        cnf_size = int(sys.argv[1])
        input_size = int(sys.argv[2])
    except IndexError:
        print 'Usage: cnf_sat_finder.py <cnf size> <number of cnf tuples>'
        sys.exit(1)

    
    generated_cnf_expression = generate_random_cnf_expression(cnf_size, input_size)
    print 'Generated CNF Expression:'
    pretty_print(generated_cnf_expression)
    
    before = time.time()
    solution, iterations = solve_cnf(generated_cnf_expression, cnf_size)
    print 'Solution:'
    pretty_print(generated_cnf_expression, solution)
    print 'Solution took %s sec to compute running %s iterations' % (time.time() - before, iterations)
#    print 'Architecture run on: \n%s' % ' '.join(os.uname()) 
        
if __name__ == '__main__':
    main()

