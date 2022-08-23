"""   
* Assignment: Function Normalize Sequence
* Required: yes
* LOC: 3

Implement funcion `normalize` which:
  * takes one argument (a sequence)
  * returns list of normalised numbers
    (numbers are scaled such the result sequence sums up to 100.0)

Tests:
    >>> normalize([1])
    [100.0]
    >>> normalize([1, 3, 4])
    [12.5, 37.5, 50.0]
    >>> result = normalize([1, 2, 3, 4])
    >>> sum(result)
    100.0
"""

# Solution


def normalize(seq):
    return [x*100/sum(seq) for x in seq]
