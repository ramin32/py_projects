#######################################################
# cnf_print.py
# A simple module with functions to pretty print a cnf 
# expression.
#######################################################

import itertools
import cnf
import sys
import os

def operator_str(operator, param='X'):
    """Returns a pretty string of the function."""
    if operator == cnf.identify:
       return 'identify(%s)' % param 
    elif operator == cnf.negate:
        return 'negate(%s)' % param 

    raise ValueError('input %s not negate or identify' % str(operator))

def create_cnf_string(cnf, booleans):
    if booleans == None:
        booleans = itertools.repeat('X')
    return " or ".join(operator_str(op, param) for op, param in zip(cnf, booleans))

def parentecize(inner_part):
    return "".join(('(',inner_part ,')'))

def cnfize(cnf, booleans):
    return parentecize(create_cnf_string(cnf, booleans))

def pretty_print(cnf_exp, solution=itertools.repeat(None)):
    zipped = zip(cnf_exp, solution)
    and_string = " and\n\t"
    cnfized_string = and_string.join(cnfize(cnf, booleans) for cnf, booleans in zipped)
    print(''.join(('\t',cnfized_string)))

def print_arch():
    if sys.platform == 'linux2':
        print('Architecture run on:')
        print(' '.join(os.uname()))
    
    

