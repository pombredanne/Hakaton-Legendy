#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 202

Napisz funkcję `calc_tf(simple_index, term, document)`, która na
podstawie zawartości indeksu oblicza liczbę wystąpień wyrazu `term`
w dokumencie o nazwie `document`.

NAME: calc_tf
PARAMS: SimpleIndex, string, string
RETURN: int
POINTS: 2
"""

import unittest
from Task202 import calc_tf
from SimpleIndex import SimpleIndex

class Task202Test(unittest.TestCase):
    """Testy do zadania 202."""

    def test(self):
        """Test do zadania 202"""

        ref_documents = {
            u'KotiKrowa': 0,
            u'SameKoty': 1,
            u'DwaPsy': 2,
            u'SameKrowy': 3}

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

        index = SimpleIndex(ref_inverted_index, ref_documents)

        ref_tfs = [
            (u"KotiKrowa", u"tekst", 1),
            (u"KotiKrowa", u"o", 2),
            (u"KotiKrowa", u"krowach", 0),
            (u"DwaPsy", u"psa", 2),
            (u"DwaPsy", u"los", 1),
            (u"DwaPsy", u"tekst", 1),
            (u"DwaPsy", u"kota", 0),
            (u"DwaPsy", u"i", 1),
            (u"SameKrowy", u"krowach", 1),
            (u"SameKrowy", u"bykach", 0),
            (u"SameKoty", u"również", 1)
        ]

        tfs = [(doc, term, calc_tf(index, term, doc))
            for (doc, term, dummy) in ref_tfs]

        self.failUnlessEqual(tfs, ref_tfs)

if __name__ == '__main__':
    unittest.main()
