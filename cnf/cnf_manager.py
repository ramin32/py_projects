##############################################################
# cnf_manager.py
#
# Module with a CnfManager implementation to manage
# Cnf objects .
###############################################################

import sys
import random
import time
import math
import itertools

import util
import cnf


class CnfManager(object):

    def __init__(self, clause_size, expression_size, variable_range):
        self.clause_size = clause_size
        self.expression_size = expression_size
        self.variable_range = variable_range
        self.function_literal_size = clause_size * expression_size

    def generate_random_clause(self):
        """Generates a cnf list."""
        return [random.choice(cnf.operators) for i in range(self.clause_size)]



    def generate_random_cnf(self):
        """Returns a randomly gnerated cnf object with the given properties."""
        generated_operator_list = [self.generate_random_clause() 
                        for i in range(self.expression_size)]

        generated_variable_list = util.generate_random_list(
                                        self.function_literal_size, 
                                        self.variable_range)
        generate_literal_list = util.group_split(generated_variable_list, self.clause_size)

        return cnf.Cnf(self, generated_operator_list, generate_literal_list)

