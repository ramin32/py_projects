#!/usr/bin/env python3.0

###############################################################################
# cnf_finder.py
#
# Usage: cnf_finder.py -clause_size <num> -exp_size <num> -variable_range <num> [-quiet]
# 
# clause_size being the size of the cnf clause, exp_size the number of 
# cnf clauses and variable_range the number of varying Xi literals to include 
# in the expression.
# 
# The actual CNF object consist of a list of tuples of functions 
# (with size clause_size) namely: identify and negate which simply return 
# either the current boolean value or its negative. 
# The CNF object also contains a list of literal tuples 
# each containing a random permutation also of size clause_size.
# 
# i.e.
# (negate , identify, negate) , (identify, identify, negate ), ...
# (0, 2, 6),  (9, 6, 2), (22, 5, 6), ...
# Due to the nature of CNF expressions the and and or operations can be 
# assumed and do not need to be stored with in the CNF object.
# 
# Once the input is generated, a for loop is run starting 
# from 0 up to 2^(variable_range). This allows each literal to properly 
# receive a boolean value by simply indexing its location in a binary string.
#
# i.e.
# To retrieve value of x3 simply execute '010010'[3] which will yield 0 or False.
# 
# Once all the literals are correctly mapped to a given permutation the 
# set of literals is plugged into the set of functions. 
# Each evaluated tuple is then or-ed and each tuple is anded with all 
# the other tuples yielding a boolean value stating whether or not the 
# current permutation is in-fact the solution.
#
############################################################################### 
# 
# 
# Usage: 
#   cnf_finder.py -clause_size <num> -exp_size <num> -variable_range <num> [-quiet]
#
# Example:
#	
#	ramin@Desktop:~/py_projects/cnf_finder$ ./cnf_finder.py  -clause_size 3 -exp_size 3 -variable_range 3 
#	Generated CNF Expression:
#		(identify(X0) or identify(X0) or identify(X0)) and
#		(identify(X1) or identify(X0) or negate(X2)) and
#		(negate(X2) or identify(X0) or negate(X1))
#		Solution: None
#	Solving...
#	Executing Iteration: #0, permutation: 000, Mapped Literal List: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#	Executing Iteration: #1, permutation: 001, Mapped Literal List: [[0, 0, 0], [0, 0, 1], [1, 0, 0]]
#	Executing Iteration: #2, permutation: 010, Mapped Literal List: [[0, 0, 0], [1, 0, 0], [0, 0, 1]]
#	Executing Iteration: #3, permutation: 011, Mapped Literal List: [[0, 0, 0], [1, 0, 1], [1, 0, 1]]
#	Executing Iteration: #4, permutation: 100, Mapped Literal List: [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
#	Done!
#		(identify(X0) or identify(X0) or identify(X0)) and
#		(identify(X1) or identify(X0) or negate(X2)) and
#		(negate(X2) or identify(X0) or negate(X1))
#		Solution: ['X0 = 1', 'X1 = 0', 'X2 = 0']
#	Solution took 0.00139284133911 sec to compute running 4/8 iterations.
#	Architecture run on: Linux Desktop 2.6.27-11-generic #1 SMP Wed Apr 1 20:53:41 UTC 2009 x86_64 
#	
# Author:
# Ramin Rakhamimov
# ramin32@gmail.com
# http://raminrakhamimov.tk
#################################################################################

import random
import time 
import sys

from cnf_finder import cnf_manager
from cnf_finder import util

def main():
    random.seed(time.time())
    try:
        clause_size = int(util.parse_arg(sys.argv, 'clause_size'))
        exp_size = int(util.parse_arg(sys.argv, 'exp_size'))
        variable_range = int(util.parse_arg(sys.argv, 'variable_range'))
    except Exception:
        print('Usage: cnf_finder.py -clause_size <num>',
                                    '-exp_size <num>',  
                                    '-variable_range <num> [-quiet]')
        sys.exit(1)

    try: 
        manager = cnf_manager.CnfManager(clause_size, exp_size, variable_range)
        generated_cnf = manager.generate_random_cnf()

        print('Generated CNF Expression:')
        print(generated_cnf)

        print('Solving...')
        before = time.time()
        iterations = generated_cnf.solve()
        print('Done!')
        print(generated_cnf)
        print('Solution took %s sec to compute running %s/%s iterations.' % 
                    (time.time() - before, iterations, 2**variable_range))

        util.print_arch()
    except KeyboardInterrupt:
        print('\n\nProgram terminated...')
    
        
if __name__ == '__main__':
    main()

