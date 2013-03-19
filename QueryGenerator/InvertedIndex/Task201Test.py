#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 201

Napisz funkcję `add_document(simple_index, document, terms)`, która
tworzy odwrócony indeks. Funkcja powinna dodawać do słownika
`simple_index.documents` kolejne nazwy dokumentów jako klucze z
przyporządkowanymi identyfikatorami (pierwszy dodany dokument ma mieć
identyfikator 0, drugi - 1 itd). Z kolei lista `terms` zawiera listę
wyrazów (termów) z dokumentu. Wyrazy mogą się powtarzać. Funkcja ma
także tworzyć indeks `simple_index.inverted_index`, czyli słownik,
który wyrazom przyporządkowuje listę identyfikatorów (czasami
wielokrotnie ten sam identyfikator, jeśli wyraz występuje więcej niż
raz dokumencie).

NAME: add_document
PARAMS: SimpleIndex, string, list
RETURN: None
POINTS: 2
"""

import unittest
from Task201 import add_document
from SimpleIndex import SimpleIndex

class Task201Test(unittest.TestCase):
    """Testy do zadania 201."""

    def test(self):
        """Test do zadania 201"""
        index = SimpleIndex({}, {})

        documents = [
            ("KotiKrowa", u"To jest krótki tekst o kocie i o krowie"),
            ("SameKoty", u"To również jest tekst o kotach"),
            ("DwaPsy", u"Ten tekst omawia los smutnego psa i radosnego psa"),
            ("SameKrowy", u"Ostatni tekst znowu o krowach")
        ]

        for document_name, text in documents:
            terms = text.lower().split()
            add_document(index, document_name, terms)

        ref_documents = {'KotiKrowa': 0,
                 'SameKoty': 1,
                 'DwaPsy': 2,
                 'SameKrowy': 3}

        ref_inverted_index = {
            u'krowach': [3],
            u'kocie': [0],
            u'ten': [2],
            u'również': [1],
            u'krótki': [0],
            u'jest': [0, 1],
            u'znowu': [3],
            u'krowie': [0],
            u'radosnego': [2],
            u'to': [0, 1],
            u'omawia': [2],
            u'psa': [2, 2],
            u'smutnego': [2],
            u'los': [2],
            u'i': [0, 2],
            u'ostatni': [3],
            u'o': [0, 0, 1, 3],
            u'kotach': [1],
            u'tekst': [0, 1, 2, 3]}

        self.failUnlessEqual(index.inverted_index, ref_inverted_index)
        self.failUnlessEqual(index.documents, ref_documents)

if __name__ == '__main__':
    unittest.main()
