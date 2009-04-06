#!/usr/bin/env python

######################################################
# 3_cnf_sat_finder.py
#
# 3-CNF-Satisfiable permutation finder.
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

def negate(b):
    """Negates the input."""
    return not b

def identity(b):
    """Returns the identity of the input."""
    return b

def generate_random_operator_tuple():
    """Generates a 3-cnf tuple."""
    operators = (negate, identity)
    return (random.choice(operators),
            random.choice(operators),
            random.choice(operators))

def create_random_3_cnf_expression(size):
    """Creates a list of 3-cnf tuples of given size."""
    expression = []
    for i in xrange(0, size, 3):
        expression.append(generate_random_operator_tuple())

    return expression

def solve(size):
    for i in xrange(2**size):
        printfoo

def operator_str(operator):
    if operator == identity:
       return 'identity',
    elif operator == negate:
        return 'negate', 
    return None

def pretty_print(cnf_exp):
    print " ^ ".join(
            [" V ".join(map(operator_str, cnf)) 
                for cnf in cnf_exp])

def main():
    random.seed(time.time())
    input_size = int(sys.argv[1])
    pretty_print(create_random_3_cnf_expression(input_size))

if __name__ == '__main__':
    main()

