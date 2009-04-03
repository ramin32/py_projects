#!/usr/bin/env python

#############################################################################
# An implementation of the classical fib routine 
# with memoization added for drastic improvements
# in running time.
# 
# As demonstrated the running time goes from linear to constant in just a few
# runs, compared to the ridiculous exponential of the original procedure.
#
# [ramin@laptop ~]$ ./fib.py
# Memoized Fib: 1.59740447998e-05 ms.
# Stupid Fib: 0.0057201385498 ms.
# Memoized Fib: 1.71661376953e-05 ms.
# Stupid Fib: 0.00943493843079 ms.
# Memoized Fib: 1.90734863281e-05 ms.
# Stupid Fib: 0.0152130126953 ms.
# Memoized Fib: 1.69277191162e-05 ms.
#
# Author:
# Ramin Rakhamimov
# ramin32@gmail.com
# http://raminrakhamimov.tk
#############################################################################

import time

fib_cache = {}

def memoized_fib(x):
    if fib_cache.has_key(x):
        return fib_cache[x]
    
    if(x < 2):
        return x
    
    fib_cache[x] = memoized_fib(x - 1) + memoized_fib(x - 2)
    return fib_cache[x]

def stupid_fib(x):
    if(x < 2):
        return x
    return stupid_fib(x - 1) + stupid_fib(x - 2)

def time_function(msg, f):
    t = time.time()
    f()
    print msg, time.time() - t, 'ms.'

def main():
    for i in xrange(0, 20):
        time_function('StupidFib(%s):' % i, 
                        lambda: stupid_fib(i))
        time_function('MemoizedFib(%s):' % i, 
                        lambda: memoized_fib(i))

if __name__ == '__main__':
    main()
