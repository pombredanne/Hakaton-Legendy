#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 27, 2013"

""" Dla funkcji 'sleep' """
import time

""" Schemat struktury odpowiedzi """
from Responses import Response

""" Wsparcie dla wyszukiwarki Blekko """
import blekko

""" Wsparcie dla wyszukiwarki DuckDuckGo """
import duckduckgo

class ResponseGatherer:
    """ Podaje linki do szukanych rzeczy """
    
    def __init__(self):
        """ Konstruktor """
        self.blekko_api = blekko.Blekko(source='my_api_key')  # Trzeba uzupełnić
        
    def get_results(self, list_of_queries):
        """
        Pobiera z wyszukiwarek linki stanowiące odpowiedź za zapytania.
        """
        
        """ Pierwsze zapytanie """
        query1 = " ".join(list_of_queries[0])
        
        """ Odpytaj Blekko """
        res_blekko = self.get_results_blekko(query1)
        
        """ Odpytaj DuckDuckGo """
        res_duck = self.get_results_duckduckgo(query1)
        
        """ Posortuj wyniki """
        list_of_lists_of_of_results = \
            [res_blekko, res_duck]
        results_sorted = self.sort_results(list_of_lists_of_of_results)
        
        return results_sorted
        
        
    def sort_results(self, list_of_lists_of_of_results):
        """
        Sortuje wyniki w odpowiedni sposób.
        Argument list_of_lists_of_of_results jest listą, której
        elementami są listy, których elementami są wyniki
        (url, tytuł, ...; czyli obiekty Response z modułu
        Responses) wyszukiwania.
        """
        
        results = []
        
        """ Liczba list z wynikami """
        num_of_lists = len(list_of_lists_of_of_results)
        
        """ Aktualne indeksy dla każdej listy. """
        indexes = [0 for i in range(num_of_lists)]
        
        # print "\nNumber of indexes: %d" % indexes
        
        for i in range(num_of_lists):
            list = list_of_lists_of_of_results[i]
            if indexes[i] < len(list):
                results.append(list[indexes[i]])
                indexes[i] = indexes[i] + 1
        
        return results
        
    def get_results_duckduckgo(self, query):
        """
        Pobiera linki z DuckDuckGo.
        """
        results = []

        r = duckduckgo.query(query)
        
        print "\nDuckDuckGo result type: %s\n" % r.type 
        
        for result in r.results:
            response = Response()
            response.url = result.url
            response.snippet = result.text
            response.engine = "DuckDuckGo"
            results.append(response)

        return results
        
        
    def get_results_blekko(self, query):
        results = []
        try:
            res = self.blekko_api.query(query)
            for result in res:
                response = Response()
                response.url_title = result.url_title
                response.url = result.url
                response.snippet = result.snippet
                response.engine = "Blekko"
                results.append(response)
                    
        except blekko.BlekkoError as exc:
            print >> sys.stderr, str(exc)
            return None
        
        return results
