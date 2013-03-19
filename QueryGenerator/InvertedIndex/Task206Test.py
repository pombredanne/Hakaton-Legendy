#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Zadanie 206

Napisz funkcję `cosine_score(simple_index, query, document)`, która dla zapytania (lista wyrazów) i zadanego dokumentu oblicza kosinus konta między wektorami zapytania i dokumentu. Wektor dokumentu powinien się składac z wartości TF-IDF (`calc_tf_idf`) dla każdego wyrazu występującego w zapytaniu oraz w całym indeksie. Wektor zapytania powinien składać się samych zer dla wyrazów niewystępujących w zapytaniu i z wartośći IDF (`calc_idf`) przemnożonych przez liczbę występowanie w zapytaniu dla wyrazów z zapytania. Wektory musza mieć oczywiście równe długości; wartości na tych samych pozycjach muszą odpowiadać tym samym wyrazom. Uwaga: w wektorach należy uwzględnić zarówno termy z kolekcji dokumentów, jak i zapytania (proszę użyć union na odpowiednich zbiorach). Należy wykorzystać rozwiązanie zadanie 204 do wyliczenia TF-IDF.

NAME: cosine_score
PARAMS: SimpleIndex, list, string
RETURN: float
POINTS: 4
"""

import unittest
from Task206 import cosine_score
from SimpleIndex import SimpleIndex

class Task206Test(unittest.TestCase):
    """Testy do zadania 206."""

    def test(self):
        """Test do zadania 206"""

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

        ref_cosines = [
            ([u'wszystko', u'o', u'kotach'], u'KotiKrowa', 0.0),
            ([u'wszystko', u'o', u'kotach'], u'SameKoty', 0.2858),
            ([u'wszystko', u'o', u'kotach'], u'DwaPsy', 0.0),
            ([u'tekst', u'dot.', u'psa'], u'SameKrowy', 0.026),
            ([u'tekst', u'dot.', u'psa'], u'DwaPsy', 0.3057)
        ]

        cosines = [(query, doc, round(cosine_score(index, query, doc), 4))
            for (query, doc, dummy) in ref_cosines]

        self.failUnlessEqual(cosines, ref_cosines)

if __name__ == '__main__':
    unittest.main()
