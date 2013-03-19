#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 205

Napisz funkcję `overlap_score(simple_index, query, document)`, która dla zapytania (lista wyrazów) i zadanego dokumentu oblicza "Overlap Score". Należy skorzystać z rozwiązania zadania 204.

NAME: overlap_score
PARAMS: SimpleIndex, list, string
RETURN: float
POINTS: 2
"""

import unittest
from Task205 import overlap_score
from SimpleIndex import SimpleIndex

class Task205Test(unittest.TestCase):
    """Testy do zadania 205."""

    def test(self):
        """Test do zadania 205"""

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

        ref_overlaps = [
            ([u'wszystko', u'o', u'kotach'], u'KotiKrowa', 0.0),
            ([u'wszystko', u'o', u'kotach'], u'SameKoty', 1.0),
            ([u'wszystko', u'o', u'kotach'], u'DwaPsy', 0.0),
            ([u'tekst', u'dot.', u'psa'], u'SameKrowy', -0.3219),
            ([u'tekst', u'dot.', u'psa'], u'DwaPsy', 1.6781)
        ]

        overlaps = [(query, doc, round(overlap_score(index, query, doc), 4))
            for (query, doc, dummy) in ref_overlaps]

        self.failUnlessEqual(overlaps, ref_overlaps)

if __name__ == '__main__':
    unittest.main()
