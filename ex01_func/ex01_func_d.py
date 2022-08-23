"""   
* Assignment: Function Vector Magnitude
* Required: yes
* LOC: 2

Implement funcion `magnitude` which:
  * takes one argument sequence: `vector`
  * returns magnitude od that vector
    (sqare root of the sum of squares of its elements)

Tests:
    >>> magnitude([3, 4])
    5.0
"""

# Solution
def magnitude(vec):
    return sum(x**2 for x in vec)**0.5
