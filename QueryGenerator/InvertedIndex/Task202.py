# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 202."""

def calc_tf(simple_index, term, document):
    """ na podstawie zawartości indeksu oblicza liczbę wystąpień wyrazu 
    term w dokumencie o nazwie document """
    
    document_index = simple_index.documents[document]
    
    if not term in simple_index.inverted_index:
	return 0
    else:
	term_occurs_in = simple_index.inverted_index[term]
    
	occurences = 0
    
	for docid in term_occurs_in:
		if docid == document_index:
			occurences = occurences + 1
             
	return occurences