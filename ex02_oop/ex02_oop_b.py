"""   
* Assignment: OOP Document

* Required: yes
* LOC: ~17

Implement class Document that stores a `text` and implements an iterator
  * `text` will be passed on as and input
  * iterator will be returning lines within text containing urls
    (i.e. lines which have 'http' string in them).

Tests:
    >>> doc = Document(text)
    >>> refs = list(doc)
    >>> len(refs)
    2
    >>> 'http://docs.python.org/' in refs[0]
    True
    >>> 'http://www.python.org/dev/peps' in refs[1]
    True
"""

text = """Most comprehensive Python language documentation
can be found on http://docs.python.org/ website

Additonal higly recommended resourece: http://www.python.org/dev/peps"""

# Solution
import re


class Document:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
       yield from re.findall(r'(https?://\S+)', text)