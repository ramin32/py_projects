************************************
*** Random Cnf Solution Finder.  ***
************************************

A brute force cnf solution finder running on randomly generated inputs.


**************
*** Usage  ***
**************

This program has been written for python 3.0 or higher. 
You must have this version of python installed to use this program.

cnf_finder.py -clause_size <num> -exp_size <num> -variable_range <num> [-quiet]

Example:
	ramin@Desktop:~/py_projects$ ./cnf_finder.py -clause_size 3 -exp_size 5 -variable_range 3 -quiet
	Generated CNF Expression:
	        (identify(X2) or negate(X1) or negate(X0)) and
	        (identify(X0) or identify(X0) or identify(X0)) and
	        (identify(X1) or identify(X2) or negate(X1)) and
	        (identify(X0) or identify(X0) or negate(X0)) and
	        (negate(X2) or identify(X2) or negate(X0))
	        Solution: None
	Solving...
	Done!
	        (identify(X2) or negate(X1) or negate(X0)) and
	        (identify(X0) or identify(X0) or identify(X0)) and
	        (identify(X1) or identify(X2) or negate(X1)) and
	        (identify(X0) or identify(X0) or negate(X0)) and
	        (negate(X2) or identify(X2) or negate(X0))
	        Solution: ['X0 = 0', 'X1 = 0', 'X2 = 0']
	Solution took 0.00039005279541 sec to compute running 0 iterations
	Architecture run on: Linux Desktop 2.6.27-11-generic #1 SMP Wed Apr 1 20:53:41 UTC 2009 x86_64 
	
**************
*** Author ***
**************

Ramin Rakhamimov
ramin32@gmail.com
http://raminrakhamimov.tk
