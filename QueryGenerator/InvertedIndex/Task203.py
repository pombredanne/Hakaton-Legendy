# -*- coding: utf-8 -*-
import math
from Task202 import *

"""Rozwiązanie zadania 203."""

def calc_idf(simple_index, term):
    """
    na podstawie zawartości indeksu oblicza wartość IDF (odwrotną częstość
    dokumentową) dla danego wyrazu. Żeby nie dzielić przez zero, liczbę
    dokumentów zawierających dany wyraz należy zwiększyć o 1.
    """
    
    if term not in simple_index.inverted_index:
        term_occurs_in = []
    else:
        term_occurs_in = simple_index.inverted_index[term]

    documents_with_term_num = len(set(term_occurs_in)) + 1.0
        
    docs_num = len(simple_index.documents)
    
    ratio = docs_num / documents_with_term_num
    
    return math.log(ratio, 2)