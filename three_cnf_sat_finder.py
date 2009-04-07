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

def identify(b):
    """Returns the identify of the input."""
    return b

def generate_random_operator_list():
    """Generates a 3-cnf list."""
    operators = (negate, identify)
    return [random.choice(operators) for i in xrange(3)]

def create_random_3_cnf_expression(size):
    """Creates a list of 3-cnf lists of given size."""
    expression = []
    for i in xrange(0, size, 3):
        expression.append(generate_random_operator_list())

    return expression


def solve_cnf(size):
    """Returns first 3-cnf-sat match using bruteforce."""
    for i in xrange(2**size):
        printfoo

def operator_str(operator):
    """Returns a pretty string of the function."""
    if operator == identify:
       return 'identify'
    elif operator == negate:
        return 'negate' 

    raise ValueError('input %s not negate or identify' % str(operator))

def pretty_print(cnf_exp):
    """Pretty prints a cnf expression."""
    create_cnf_string = lambda cnf: " V ".join(map(operator_str, cnf))
    parentecize = lambda inner_part: "".join(('(',inner_part ,' )'))

    print " ^ ".join([parentecize(create_cnf_string(cnf)) for cnf in cnf_exp])

def main():
    random.seed(time.time())
    input_size = int(sys.argv[1])
    pretty_print(create_random_3_cnf_expression(input_size))

if __name__ == '__main__':
    main()

