#!/usr/bin/env python

######################################################
# 3_cnf_sat_finder.py
#
# 3-CNF-Satisfiable permutation finder.
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
######################################################

import sys
import random
import time
import math

# TODO Move all cnf logic into a cnf class

"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

def generate_cnf():
    """Generates a 3-cnf list."""
    operators = (negate, identify)
    return [random.choice(operators) for i in xrange(3)]

def create_random_3_cnf_expression(size):
    """Creates a list of 3-cnf lists of given size."""
    return [generate_cnf() for i in xrange(size)]

def create_boolean_groups(x, max_size):
    """Constructs binary groups of size 3 taken from splitting 
    the binary string representation of x."""
    raw_binary = bin(x)[2:].zfill(max_size)                    # strip the 0b header and pad with 0's
    booleans = [{'0': False, '1':True}[b] for b in raw_binary] # map 0's and 1's to booleans
    binary_groups = group_split(booleans, 3) 
    return binary_groups

def group_split(seq, size):
    """Splits the given sequence into groups of size."""
    return [seq[i:i+size] for i in range(0, len(seq), size)]


def evaluate_cnf_with_booleans(cnf_exp, boolean_groups):
    """Plugs in the binary string into the cnf expression evaluating to true or false."""
    zipped = zip(cnf_exp, boolean_groups)
    evaluate_cnf = lambda z: any([z[0][i](z[1][i]) for i in xrange(3)])
    cnf_evaluations = map(evaluate_cnf, zipped)
    return all(cnf_evaluations)

def solve_cnf(cnf_exp):
    """Returns first 3-cnf-sat match using bruteforce."""
    size = len(cnf_exp) * 3
    for i in xrange(2**size):
        boolean_groups = create_boolean_groups(i, size)
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
    input_size = int(sys.argv[1])
    
    generated_cnf_expression = create_random_3_cnf_expression(input_size)
    print 'Generated 3-CNF Expression:'
    pretty_print(generated_cnf_expression)
    
    solution = solve_cnf(generated_cnf_expression)
    print 'Solution:'
    print solution
        
if __name__ == '__main__':
    main()

