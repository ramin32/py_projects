#####################################################
# util.py
#
# Utilitiy module for various helper functions.
#####################################################

import random
import sys
import platform

def group_split(seq, size):
    """Splits the given sequence into groups of given size."""
    return [seq[i:i + size] for i in range(0, len(seq), size)]
      
def print_arch():
    """Prints the arch name (only work on linux)."""
    if sys.platform == 'linux2':
        print('Architecture run on: %s' % ' '.join(platform.uname()))

def parentecize(inner_part):
    """Returns a parentecized string."""
    return '(%s)' % inner_part

def padded_binary(x, max_size):
    """Returns a binary string representation of x.
    Padded with 0 at the right."""

    # strip the 0b hex header and pad with 0's
    raw_binary = bin(x)[2:].zfill(max_size)                   
    return raw_binary

def generate_random_list(size, item_range):
    """Returns a randomized list of given size with elements within a range."""
    print(size,range)
    return [random.randint(0, item_range - 1) for i in range(size)]

