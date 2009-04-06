#!/usr/bin/env python

import random
import time

random.seed(time.time())

def print_list(list):
    for i in list:
        print i,
    print

def partition(list, start, end):
    pivot = list[random.randint(start, end)]
    while True:
        while list[start] < pivot:
            start += 1
        while list[end] > pivot:
            end -= 1

        if start >= end:
            return start

        list[start], list[end] = list[end], list[start]

def quicksort(list, start, end):
    if start >= end:
        return
    pivot = partition(list, start, end)
    partition(list, start, pivot)
    partition(list, pivot, end)

def main():
    l = range(100)
    l2 = []
    for i in xrange(10):
        l2.append(random.choice(l))

    print 'Unordered list: %' % l2

    quicksort(l2, 0, len(l2)-1)
    print 'Ordered list: %' % l2

if __name__ == '__main__':
    main()




