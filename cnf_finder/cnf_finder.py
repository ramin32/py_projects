#!/usr/bin/env python3.0

###############################################################################
# cnf_finder.py
#
# CNF-Satisfiable solution finder.
#
# Description:
# Permutes through all the boolean variations from 0 till 2^n
# Plugs in each boolean permutation into the cnf expression 
# until a solution is found.
#
# cnf expressions are represented as a list of tuples 
# containing either of the following 2 lambda functions:
#   negate = lambda b: not b
#   identify = lambda b: b
# The literals are grouped together in a seperate list.
# ie: ((0, 2, 1), (0, 2, 3), (0, 1, 1)) => ((X0, X2, X1), (X0, X2, X3), (X0, X1, X1))
# 
# These cnf expressions are randomly generated in to which the boolean 
# permutations are plugged into to evaluate its truthiness.
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

