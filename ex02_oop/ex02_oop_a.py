"""   
* Assignment: OOP Document

* Required: yes
* LOC: ~17

Zaimplementuj klasę Document zawierającą pole tekstowe oraz listę referencji, które
będą linkami użytymi w dokumencie (dla ułatwienia referencje mogą to być całe linie
tekstu w których występuje tekst “http://”). Lista referencji zostanie automatycznie
utworzona przy inicjalizacji dokumentu.

Implement class Document that stores a `text` and a list of `references`.
  * `text` will be passed on as and input
  * `references` will be dynamically calculated list of lines within text
    containing urls (i.e. lines which have 'http' string in them).

Tests:
    >>> doc = Document(text)
    >>> len(doc.references)
    2
    >>> 'http://docs.python.org/' in doc.references[0]
    True
    >>> 'http://www.python.org/dev/peps' in doc.references[1]
    True
"""

text = """Most comprehensive Python language documentation
can be found on http://docs.python.org/ website

Additonal higly recommended resourece: http://www.python.org/dev/peps"""

# Solution
import re


class Document:
    def __init__(self,text):
        self.references = re.findall(r'(https?://\S+)', text)
