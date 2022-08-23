"""   
* Assignment: Higher Order Functon Reduce Pairs

* Required: yes
* LOC: 7

Implement higher order generator function `reduce_pairs` which takes two arguments:
2-argument function: `func` and a sequence
  * `func` will be applied to neighbouring elements of sequence
  * result list will have length of half of input sequence.
    [func(seq[0], seq[1]),
     func(seq[2], seq[3]),
     ...]

Tests:
    >>> def concat(a, b):
    ...    return f"{a}|{b}"
    >>> list(reduce_pairs(concat, [1, 2, 3, 4, 5, 6]))
    ['1|2', '3|4', '5|6']
    >>> def add(a, b):
    ...    return a + b
    >>> list(reduce_pairs(add, [1, 2, 3, 4, 5, 6]))
    [3, 7, 11]
"""

# Solution


def reduce_pairs(func, seq):
    return [func(x,y) for x,y in zip(seq[::2], seq[1::2])]