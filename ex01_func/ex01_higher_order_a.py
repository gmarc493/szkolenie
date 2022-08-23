"""   
* Assignment: Decorator Reduce Pairs
* Required: yes
* LOC: 4

Implement decorator `reduce_pairs` which can decorate a 2-argiment function:
  * decorator will take one argument sequence with even number of elemenst
  * decorated function will be applied to neighbouring elements of input sequence
  * result list will have length of half of input sequence.
    [orig_func(seq[0], seq[1]),
     orig_func(seq[2], seq[3]),
     ...]

Tests:
    >>> @reduce_pairs
    ... def concat(a, b):
    ...    return f"{a}|{b}"
    >>> list(concat([1, 2, 3, 4, 5, 6]))
    ['1|2', '3|4', '5|6']
    >>> @reduce_pairs
    ... def add(a, b):
    ...    return a + b
    >>> list(add([1, 2, 3, 4, 5, 6]))
    [3, 7, 11]
"""

# Solution


def reduce_pairs(func):
    def wrapped(seq):
        return [func(x,y) for x,y in zip(seq[::2], seq[1::2])]
    return wrapped