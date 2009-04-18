#######################################################
# cnf_print.py
# A simple module with functions to pretty print a cnf 
# expression.
#######################################################

import itertools
import cnf
import sys
import os

import util
import cnf_manager

"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

operators = (negate, identify)

class Cnf(object):

    def __init__(self, manager, function_list, literal_list):
        self.manager = manager
        self.function_list = function_list
        self.literal_list = literal_list
        self.solution = itertools.repeat(None)

    @staticmethod
    def operator_str(operator, param='X'):
        """Returns a pretty string of the function."""
        if operator == identify:
           return 'identify(%s)' % param 
        elif operator == negate:
            return 'negate(%s)' % param 

        raise ValueError('input %s not negate or identify' % str(operator))

    @staticmethod
    def create_cnf_string(cnf, booleans):
        if booleans == None:
            booleans = itertools.repeat('X')
        return " or ".join(Cnf.operator_str(op, param) for op, param in zip(cnf, booleans))

    @staticmethod
    def cnfize(cnf, booleans):
        return util.parentecize(Cnf.create_cnf_string(cnf, booleans))

    def __str__(self):
        zipped = zip(self.function_list, self.solution)
        and_string = " and\n\t"
        cnfized_string = and_string.join(Cnf.cnfize(cnf, booleans) for cnf, booleans in zipped)
        return ''.join(('\t',cnfized_string))


    def evaluate(self, boolean_groups):
        """Plugs in the binary string into the cnf expression 
        evaluating to true or false."""
        return all(any(f(b) for f,b in zip(clause, booleans)) 
                   for clause, booleans in zip(self.function_list, boolean_groups))

    def solve(self):
        """Returns first cnf-sat match using bruteforce."""
        iterations = 0
        variable_permutation_size = 2**self.manager.variable_range
        for i in range(0, variable_permutation_size):
            permutation = util.padded_binary(i, variable_permutation_size)[::-1]
            
            mapped_literal_list =list(map(lambda i,l: permutation[i], itertools.count(0), self.literal_list))
            boolean_groups = util.group_split(mapped_literal_list, self.manager.clause_size)
            if self.evaluate(boolean_groups):
                self.solution = boolean_groups
                break
            iterations += 1
        return iterations

