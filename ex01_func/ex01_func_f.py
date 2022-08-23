"""   
* Assignment: Function Factorial
* Required: yes
* LOC: 4

Implement funcion `factorial` which:
  * takes one argument int: `n``
  * returns facorial of `n`

Tests:
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(5)
    120

Hint:
    * use recurrence

"""

# Solution
def factorial(n):
    if n <= 2:
        return n
    return n * factorial(n-1)


def factorial(n):
    acc = 1
    for x in range(1, n+1):
        acc *= x
    return acc

