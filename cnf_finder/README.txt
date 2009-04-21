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

ramin@Desktop:~/py_projects/cnf_finder$ ./cnf_finder.py  -clause_size 3 -exp_size 3 -variable_range 3 
Generated CNF Expression:
	(identify(X0) or identify(X0) or identify(X0)) and
	(identify(X1) or identify(X0) or negate(X2)) and
	(negate(X2) or identify(X0) or negate(X1))
	Solution: None
Solving...
Executing Iteration: #0, permutation: 000, Mapped Literal List: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Executing Iteration: #1, permutation: 001, Mapped Literal List: [[0, 0, 0], [0, 0, 1], [1, 0, 0]]
Executing Iteration: #2, permutation: 010, Mapped Literal List: [[0, 0, 0], [1, 0, 0], [0, 0, 1]]
Executing Iteration: #3, permutation: 011, Mapped Literal List: [[0, 0, 0], [1, 0, 1], [1, 0, 1]]
Executing Iteration: #4, permutation: 100, Mapped Literal List: [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
Done!
	(identify(X0) or identify(X0) or identify(X0)) and
	(identify(X1) or identify(X0) or negate(X2)) and
	(negate(X2) or identify(X0) or negate(X1))
	Solution: ['X0 = 1', 'X1 = 0', 'X2 = 0']
Solution took 0.00139284133911 sec to compute running 4/8 iterations.
Architecture run on: Linux Desktop 2.6.27-11-generic #1 SMP Wed Apr 1 20:53:41 UTC 2009 x86_64 
	
**************
*** Author ***
**************

Ramin Rakhamimov
ramin32@gmail.com
http://raminrakhamimov.tk
