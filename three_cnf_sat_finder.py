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
import math

"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

def generate_random_operator_list():
    """Generates a 3-cnf list."""
    operators = (negate, identify)
    return tuple([random.choice(operators) for i in xrange(3)])

def create_random_3_cnf_expression(size):
    """Creates a list of 3-cnf lists of given size."""
    expression = []
    for i in xrange(size):
        expression.append(generate_random_operator_list())

    return tuple(expression)

def padded_binary(x, max_size):
    """Returns x as a binary string padded with 0's upto max_size."""
    binary = bin(x)[2:]
    padding_left = max_size - len(binary)
    if padding_left > 0:
        binary = ''.join((''.join(['0' for i in xrange(padding_left)]), binary))
    return binary
            
def evaluate_cnf(cnf_exp, binary_string):
    """Plugs in the binary string into the cnf expression evaluating to true or false."""
    pass



def solve_cnf(cnf_exp):
    """Returns first 3-cnf-sat match using bruteforce."""
    size = len(cnf_exp) * 3
    for i in xrange(2**size):
        binary_string = padded_binary(i, size)
        if evaluate_cnf(cnf_exp, binary_string):
            return binary_string
    return None


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
    
    generated_cnf_expression = create_random_3_cnf_expression(input_size)
    print 'Generated 3-CNF Expression:'
    pretty_print(generated_cnf_expression)
    
    solution = solve_cnf(generated_cnf_expression)
    print 'Solution:'
    print solution



if __name__ == '__main__':
    main()

