#!/usr/bin/env python

###############################################################################
# three_cnf_sat_finder.py
#
# 3-CNF-Satisfiable solution finder.
#
# Description:
# Permutes through all the boolean variations from 0 till 2^n
# Plugs in each boolean permutation into the cnf expression 
# until a solution is found.
#
# 3-cnf expressions are represented as a list of tuples (of size 3)
# containing either of the following 2 lambda functions:
#   negate = lambda b: not b
#   identify = lambda b: b
# 
# These 3-cnf expressions are randomly generated in to which the boolean permutations
# are plugged into to evaluate its truthiness.
#
############################################################################### 
# 
# 
# Usage: 
#   three_cnf_sat_finder.py <number of cnf tuples>
#
# Example:
#   [ramin@desktop py_projects]$ ./three_cnf_sat_finder.py 3
#   Generated 3-CNF Expression:
#        (negate(X) V identify(X) V identify(X)) ^ 
#        (identify(X) V negate(X) V identify(X)) ^ 
#        (negate(X) V identify(X) V negate(X))
#    
#   Solution:
#       [[False, False, False], [False, False, False], [False, False, False]]
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

# TODO Move all cnf logic into a cnf class


"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

def forloop(start, end):
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
    """Plugs in the binary string into the cnf expression evaluating to true or false."""
    return all(any(f(b) for f,b in itertools.izip(cnf,booleans)) for cnf, booleans in itertools.izip(cnf_exp, boolean_groups))

def solve_cnf(cnf_exp, cnf_size):
    """Returns first cnf-sat match using bruteforce."""
    size = len(cnf_exp) * cnf_size
    for i in forloop(0, 2**size):
        boolean_groups = create_boolean_groups(i, size, cnf_size)
        if evaluate_cnf_with_booleans(cnf_exp, boolean_groups):
            return boolean_groups
    return None


def operator_str(operator, param='X'):
    """Returns a pretty string of the function."""
    if operator == identify:
       return 'identify(%s)' % param 
    elif operator == negate:
        return 'negate(%s)' % param 

    raise ValueError('input %s not negate or identify' % str(operator))

def pretty_print(cnf_exp):
    """Pretty prints a cnf expression."""
    create_cnf_string = lambda cnf: " V ".join(map(operator_str, cnf))
    parentecize = lambda inner_part: "".join(('(',inner_part ,')'))

    print " ^ ".join([parentecize(create_cnf_string(cnf)) for cnf in cnf_exp])

def main():
    random.seed(time.time())
    try:
        cnf_size = int(sys.argv[1])
        input_size = int(sys.argv[2])
    except IndexError:
        print 'Usage: three_cnf_sat_finder.py <cnf size> <number of cnf tuples>'
        sys.exit(1)

    
    generated_cnf_expression = generate_random_cnf_expression(cnf_size, input_size)
    print 'Generated CNF Expression:'
    pretty_print(generated_cnf_expression)
    
    solution = solve_cnf(generated_cnf_expression, cnf_size)
    print 'Solution:'
    print solution
        
if __name__ == '__main__':
    main()

