#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 203

Napisz funkcję `calc_idf(simple_index, self, term)`, która na
podstawie zawartości indeksu oblicza wartość IDF (odwrotną częstość
dokumentową) dla danego wyrazu. Żeby nie dzielić przez zero, liczbę
dokumentów zawierających dany wyraz należy zwiększyć o 1. Przez to
wartość IDF może przyjąć wartości ujemne w przypadku, gdy wyraz
występuje we wszystkich dokumentach, co jest mało prawdopodobne w
przypadku dużych zbiorów.

NAME: calc_idf
PARAMS: SimpleIndex, string
RETURN: float
POINTS: 3
"""

import unittest
from Task203 import calc_idf
from SimpleIndex import SimpleIndex

class Task203Test(unittest.TestCase):
    """Testy do zadania 203."""

    def test(self):
        """Test do zadania 203"""

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

        ref_idfs = [
            (u'tekst', -0.3219),
            (u'o', 0.0),
            (u'krowach', 1.0),
            (u'psa', 1.0),
            (u'los', 1.0),
            (u'kota', 2.0),
            (u'i', 0.415),
            (u'krowach', 1.0),
            (u'bykach', 2.0),
            (u'również', 1.0)
        ]

        idfs = [(term, round(calc_idf(index, term), 4))
            for (term, dummy) in ref_idfs]

        self.failUnlessEqual(idfs, ref_idfs)

if __name__ == '__main__':
    unittest.main()
