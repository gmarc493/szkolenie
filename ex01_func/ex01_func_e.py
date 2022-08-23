"""   
* Assignment: Function Dot Product
* Required: yes
* LOC: 2

Implement funcion `dot_product` which:
  * takes two arguments sequence: `vector`` and sequence `vector2`
  * returns dot product of two vectors (sum of elementwise multiplication)

Tests:
    >>> vec1 = [1, 2, 3]
    >>> vec2 = [4, 5, 6]
    >>> dot_product(vec1, vec2)  # (1 * 4) + (2 * 5) + (3 * 6)
    32

Hint:
    * dot_product([1, 2], [3, 4]) == (1 * 3) + (2 * 4)

"""

# Solution


def dot_product(vector, vector2):
    return sum([x*y for x, y in zip(vector, vector2)])
