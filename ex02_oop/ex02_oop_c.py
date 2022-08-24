"""   
* Assignment: OOP Document

* Required: yes
* LOC: ~22

Implement class `Vector` extending class `VectorBase`:
  * implementation of `+` operator for for types: `Vector`, `list`, `Number`
  * implementation of all missing !=, <, >=, <= comparison operators based
    on alredy implemented ones (== and >).

Tests:
    >>> v1 = Vector([1, 1])
    >>> v1
    Vector[1, 1]
    >>> v1 + Vector([-1, -3])
    Vector[0, -2]
    >>> v1 + [-1, 11]
    Vector[0, 12]
    >>> v1 + 3.1
    Vector[4.1, 4.1]
    >>> Vector([5, 1]) == Vector([1, 5])
    True
    >>> Vector([1, 5]) > Vector([2, 1])
    True
    >>> Vector([1, 5]) < Vector([2, 1])
    False

Hints:
  * use `functools.singledispatchmethod`
  * discuss why `total_ordering` might not work
"""
from functools import cached_property, singledispatchmethod
from numbers import Number
import math

class VectorBase(list):

    def __eq__(self, other):
        return self.magnitude == other.magnitude

    def __gt__(self, other):
        return self.magnitude > other.magnitude

    def __add__(self, other):
        raise NotImplementedError(
                f"Cannot add type `{type(other)!r}` to Vector")

    def __mul__(self, scalar):
        "Scale Vector by scalar. Returns new scaled Vector instance."
        return Vector([x*other for x in self])

    def __repr__(self):
        return f"Vector{super().__repr__()}"

    @cached_property
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self))

# Solution
class Vector(VectorBase):

    def __add__(self, other):
        if not isinstance(other, (Vector, list, Number)):
            raise TypeError("wrong type!")
        if isinstance(other, (Vector, list)):
            return Vector([x+y for x,y in zip(self,other)])
        elif isinstance(other, Number):
            return Vector([x+other for x in self])