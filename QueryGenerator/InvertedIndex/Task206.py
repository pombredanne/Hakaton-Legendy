# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 206."""

from Task203 import calc_idf
from Task204 import calc_tf_idf
from math import sqrt

def list_of_all_terms(simple_index, query):
    """
    Buduje listę wszystkich termów występujących w zapytaniu oraz
    w indeksie
    """
    
    all_terms = []
    
    for key in simple_index.inverted_index.keys():
        if not key in all_terms:
            all_terms.append(key)
    
    for term in query:
        if not term in all_terms:
            all_terms.append(term)
    
    return all_terms
            
            
def document_vector(simple_index, document, all_terms):
    """
    Wektor dokumentu powinien się składac z wartości 
    TF-IDF (`calc_tf_idf`) dla każdego wyrazu występującego 
    w zapytaniu oraz w całym indeksie.
    """
    
    vector = []
    
    for term in all_terms:
        vector.append(calc_tf_idf(simple_index, term, document))
    
    return vector
            

def query_vector(simple_index, query, all_terms):
    """
    Wektor zapytania powinien składać się samych zer dla
    wyrazów niewystępujących w zapytaniu i z wartośći 
    IDF (`calc_idf`) przemnożonych przez liczbę występowanie
    w zapytaniu dla wyrazów z zapytania.
    """

    vector = []
    
    for term in all_terms:
        if not term in query:
            vector.append(0)
        else:
            idf = calc_idf(simple_index, term) * query.count(term)
            vector.append(idf)
            
    return vector


def euclid_len(vector):
    """
    Długość euklidesowa wektora.
    """
    
    length = 0
    for i in range(len(vector)):
        length = length + (vector[i] * vector[i])
        
    length = sqrt(length)
        
    return length
    

def vectors_cosine(vector_a, vector_b):
    """
    Liczy kosinus kąta między wektorami.
    """
    
    dot_product = 0
    for i in range(len(vector_a)):
        dot_product = dot_product + (vector_a[i] * vector_b[i])
        
    length_a = euclid_len(vector_a)
    length_b = euclid_len(vector_b)
    
    return dot_product / (length_a * length_b)
       

def cosine_score(simple_index, query, document):
    """
    dla  zadanego dokumentu oblicza kosinus kąta 
    między wektorami zapytania i dokumentu
    """
    
    all_terms = list_of_all_terms(simple_index, query)

    document_v = document_vector(simple_index, document, all_terms)
    
    query_v = query_vector(simple_index, query, all_terms)
            
    return vectors_cosine(document_v, query_v)
