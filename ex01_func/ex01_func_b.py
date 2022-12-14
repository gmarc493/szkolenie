"""   
* Assignment: Function Scale Vector
* Required: yes
* LOC: 5

Implement funcion `scale` which:
  * takes two arguments scalar: `n` and sequence `vector`
  * returns list of `vector` elements scaled (multiplied) by `n`

Tests:
    >>> scale(3, [1, 2, 3, 4, 5])
    [3, 6, 9, 12, 15]
    >>> scale(0.5, [4, 2, 1])
    [2.0, 1.0, 0.5]
"""

# Solution


def scale(n, vector):
    return [x*n for x in vector]