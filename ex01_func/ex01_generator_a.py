"""   
* Assignment: Generator Countdown
* Required: yes
* LOC: 4 

Implement generator `countdown` which:
  * takes one argument int: `n`
  * on iteration returns elements starting from `n` to 0 (inclusive)

Tests:
    >>> c = countdown(10)
    >>> list(c)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

# Solution
def countdown(n):
    while n>= 0:
        yield n
        n -= 1