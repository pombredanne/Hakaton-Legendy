# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 205."""

from Task204 import calc_tf_idf

def overlap_score(simple_index, query, document):
    
    """
    która dla zapytania (lista wyrazów) i zadanego 
    dokumentu oblicza 'Overlap Score'
    """
    
    o_scope = 0
    for term in query:
        o_scope += calc_tf_idf(simple_index, term, document)
    
    return o_scope
