# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 204."""

from Task202 import calc_tf
from Task203 import calc_idf

def calc_tf_idf(simple_index, term, document):
    
    """ Liczy tf-idf """
    
    return calc_tf(simple_index, term, document) * calc_idf(simple_index, term)
