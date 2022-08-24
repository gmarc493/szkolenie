"""   
* Assignment: Generator Random Walk
* Required: yes
* LOC: 2

Implement generator `randomwalk` which:
  * takes one argument sequence: `seq`
  * on iteration returns random elemens from `seq` without repetition.

Tests:
    >>> re = randomwalk([1])
    >>> list(re)
    [1]
    >>> list(randomwalk('abcdef'))
    ['d', 'a', 'c', 'f', 'b', 'e']
    >>> list(randomwalk(range(10)))
    [4, 7, 5, 9, 1, 6, 8, 3, 0, 2]
"""
import random
random.seed(0)

# Solution
