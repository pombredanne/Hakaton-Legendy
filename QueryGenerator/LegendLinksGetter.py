#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 25, 2013"

from QueryGenerator import QueryGenerator

from ResponseGatherer import ResponseGatherer

class LegendLinksGetter:
    """
    Pobiera wyniki wyszukiwania z różnych przeglądarek.
    """
    
    def __init__(self):
        """ Konstruktor... """
        self.query_generator = QueryGenerator()
        self.response_gatherer = ResponseGatherer()
    
    def search(self, legend_text):
        """
        Szuka w Internetach linków do legend.
            legend_text jest pełnym tekstem legendy.
        Metoda zwraca listę wyników. Wynik w ma pola:
            w.url_title - tytuł
            w.url - adres url
            w.snippet - fragment
            w.engine - wyszukiwarka
        """
        queries = self.query_generator.generate_queries(legend_text)
        results = self.response_gatherer.get_results(queries)
        
        return results
