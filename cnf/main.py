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
#   cnf_sat_finder.py <cnf size> <number of cnf tuples>
#
# Example:
#   [ramin@laptop py_projects]$ ./cnf_sat_finder.py 3 3
#   Generated CNF Expression:
#       (identify(X) or identify(X) or identify(X)) and
#       (identify(X) or negate(X) or identify(X)) and
#       (identify(X) or negate(X) or identify(X))
#   Solution:
#       (identify(False) or identify(False) or identify(True)) and
#       (identify(False) or negate(False) or identify(False)) and
#       (identify(False) or negate(False) or identify(False))
#   Solution took 0.00402617454529 sec to compute running 64 iterations
#   Architecture run on: 
#   Linux laptop 2.6.29-ARCH #1 SMP PREEMPT Tue Apr 7 12:47:56 UTC 2009 i686
#   
#
#
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
        clause_size = int(sys.argv[1])
        input_size = int(sys.argv[2])
        variable_range = int(sys.argv[3])
    except IndexError:
        print('Usage: cnf_sat_finder.py <clause_size> <expression_size> <variable_range>')
        sys.exit(1)

    try: 
        manager = cnf_manager.CnfManager(clause_size, input_size, variable_range)
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

