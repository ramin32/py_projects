#!/usr/bin/env python3.0

###############################################################################
# main.py
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
# 
# These cnf expressions are randomly generated in to which the boolean 
# permutations are plugged into to evaluate its truthiness.
#
############################################################################### 
# 
# 
# Usage: 
#   ./main.py -clause_size <num> -exp_size <num> -variable_range <num>
#   cnf_sat_finder.py <cnf size> <number of cnf tuples>
#
# Example:
#	
#	ramin@Desktop:~/py_projects/cnf$ ./main.py -clause_size 3 -exp_size 5 -variable_range 3
#	Generated CNF Expression:
#	        (identify(X2) or negate(X1) or negate(X0)) and
#	        (identify(X0) or identify(X0) or identify(X0)) and
#	        (identify(X1) or identify(X2) or negate(X1)) and
#	        (identify(X0) or identify(X0) or negate(X0)) and
#	        (negate(X2) or identify(X2) or negate(X0))
#	        Solution: None
#	Solving...
#	Done!
#	        (identify(X2) or negate(X1) or negate(X0)) and
#	        (identify(X0) or identify(X0) or identify(X0)) and
#	        (identify(X1) or identify(X2) or negate(X1)) and
#	        (identify(X0) or identify(X0) or negate(X0)) and
#	        (negate(X2) or identify(X2) or negate(X0))
#	        Solution: ['X0 = 0', 'X1 = 0', 'X2 = 0']
#	Solution took 0.00039005279541 sec to compute running 0 iterations
#	Architecture run on: Linux Desktop 2.6.27-11-generic #1 SMP Wed Apr 1 20:53:41 UTC 2009 x86_64 
#	
# Author:
# Ramin Rakhamim# Usage: 
#   ./main.py -clause_size <num> -exp_size <num> -variable_range <num>
#   cnf_sat_finder.py <cnf size> <number of cnf tuples>
#
# Example:
#       
#       ramin@Desktop:~/py_projects/cnf$ ./main.py -clause_size 3 -exp_size 5 -variable_range 3
#       Generated CNF Expression:
#               (identify(X2) or negate(X1) or negate(X0)) and
#               (identify(X0) or identify(X0) or identify(X0)) and
#               (identify(X1) or identify(X2) or negate(X1)) and
#               (identify(X0) or identify(X0) or negate(X0)) and
#               (negate(X2) or identify(X2) or negate(X0))
#               Solution: None
#       Solving...
#       Done!
#               (identify(X2) or negate(X1) or negate(X0)) and
#               (identify(X0) or identify(X0) or identify(X0)) and
#               (identify(X1) or identify(X2) or negate(X1)) and
#
# Author:
# Ramin Rakhamimov
# ramin32@gmail.com
# http://raminrakhamimov.tk
#################################################################################

import random
import time 
import sys

import cnf_manager
import util

def main():
    random.seed(time.time())
    try:
        clause_size = int(util.parse_arg(sys.argv, 'clause_size'))
        exp_size = int(util.parse_arg(sys.argv, 'exp_size'))
        variable_range = int(util.parse_arg(sys.argv, 'variable_range'))
    except Exception:
        print('Usage: .main.py -clause_size <num> -exp_size <num> -variable_range <num>')
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
        print('Solution took %s sec to compute running %s iterations' % (time.time() - before, iterations))

        util.print_arch()
    except KeyboardInterrupt:
        print('Program terminated...')
    
        
if __name__ == '__main__':
    main()

