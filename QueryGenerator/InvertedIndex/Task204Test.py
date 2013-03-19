#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 204

Napisz funkcję `calc_tf_idf(simple_index, term, document)`, która na podstawie zawartości indeksu oblicza wartość TF-IDF dla danego wyrazu i dokumentu. Nalezy oczywiście wykorzystać funkcje `calc_tf` oraz `calc_idf` (nie ma więc sensu rozwiązywać to zadanie bez wcześniejszego rozwiązania zadań 202 i 203).

NAME: calc_tf_idf
PARAMS: SimpleIndex, string, string
RETURN: float
POINTS: 1
"""

import unittest
from Task204 import calc_tf_idf
from SimpleIndex import SimpleIndex

class Task204Test(unittest.TestCase):
    """Testy do zadania 204."""

    def test(self):
        """Test do zadania 204"""

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

        ref_tf_idfs = [
            (u'KotiKrowa', u'tekst', -0.3219),
            (u'KotiKrowa', u'o', 0.0),
            (u'KotiKrowa', u'krowach', 0.0),
            (u'DwaPsy', u'psa', 2.0),
            (u'DwaPsy', u'los', 1.0),
            (u'DwaPsy', u'tekst', -0.3219),
            (u'DwaPsy', u'kota', 0.0),
            (u'DwaPsy', u'i', 0.415),
            (u'SameKrowy', u'krowach', 1.0),
            (u'SameKrowy', u'bykach', 0.0),
            (u'SameKoty', u'również', 1.0)
        ]

        tf_idfs = [(doc, term, round(calc_tf_idf(index, term, doc), 4))
            for (doc, term, dummy) in ref_tf_idfs]

        self.failUnlessEqual(tf_idfs, ref_tf_idfs)

if __name__ == '__main__':
    unittest.main()
