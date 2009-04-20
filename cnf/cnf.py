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

import pdb

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
        self.solution = None

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
        return " or ".join(Cnf.operator_str(op, ''.join(('X',str(param)))) for op, param in zip(cnf, booleans))

    @staticmethod
    def cnfize(cnf, booleans):
        return util.parentecize(Cnf.create_cnf_string(cnf, booleans))

    def __str__(self):
        zipped = zip(self.function_list, self.literal_list)
        and_string = ' and\n\t'
        cnfized_string = and_string.join(Cnf.cnfize(cnf, booleans) for cnf, booleans in zipped)

        solution = 'None'
        if self.solution:
            solution = ['X%s = %s' % (i, value) for i, value in zip(itertools.count(0), self.solution)]

        return '\t %s \n\tSolution: %s' % (cnfized_string, solution)


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
            # obtain the binary representation of permutation and reverse it
            permutation = util.padded_binary(i, self.manager.variable_range)[::-1]
            #pdb.set_trace()
            
            # map 
            mapped_literal_list = [[permutation[item] for item in clause] 
                                                        for clause in self.literal_list]
            if self.evaluate(mapped_literal_list):
                self.solution = permutation
                break
            iterations += 1
        return iterations

