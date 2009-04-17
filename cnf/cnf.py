##############################################################
# cnf.py
# Module with a CnfManager implementation to manage
# cnf exressions.
###############################################################

import sys
import random
import time
import math
import itertools


"""Negates the input."""
negate = lambda b: not b

"""Returns the identify of the input."""
identify = lambda b: b

class CnfManager(object):

    def __init__(self, clause_size, expression_size, variable_range):
        self.clause_size = clause_size
        self.expression_size = expression_size
        self.variable_range = clause_size * expression_size

    def generate_random_clause(self):
        """Generates a cnf list."""
        operators = (negate, identify)
        return [random.choice(operators) for i in range(self.clause_size)]

    def generate_random_variable_list(self):
        var_list = []
        list_size = self.clause_size * self.expression_size
        for i in range(list_size):
            var_list.append(random.randint(0, self.variable_range - 1))
        return var_list


    def generate_random_expression(self):
        """Creates a list of cnf lists of given size."""
        return [self.generate_random_clause() 
                        for i in range(self.expression_size)]

    def create_boolean_groups(self, x, max_size):
        """Constructs binary groups of the cnf size taken from splitting 
        the binary string representation of x."""

        # strip the 0b hex header and pad with 0's
        raw_binary = bin(x)[2:].zfill(max_size)                   
        # map 0's and 1's to booleans
        booleans = [{'0': False, '1':True}[b] for b in raw_binary] 
        # split booleans list into tuples of cnf size
        binary_groups = self.group_split(booleans)            
        return binary_groups

    def group_split(self, seq):
        """Splits the given sequence into groups of size."""
        return [seq[i:i+self.clause_size] 
                    for i in range(0, len(seq), self.clause_size)]


    @staticmethod
    def evaluate(cnf_exp, boolean_groups):
        """Plugs in the binary string into the cnf expression 
        evaluating to true or false."""
        return all(any(f(b) for f,b in zip(clause, booleans)) 
                   for clause, booleans in zip(cnf_exp, boolean_groups))

    def solve(self, cnf_exp):
        """Returns first cnf-sat match using bruteforce."""
        size = len(cnf_exp) * self.clause_size
        iterations = 0
        for i in range(0, 2**size):
            boolean_groups = self.create_boolean_groups(i, size)
            if self.evaluate(cnf_exp, boolean_groups):
                return boolean_groups, iterations
            iterations += 1
        return None, iterations

