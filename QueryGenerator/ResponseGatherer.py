#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 24, 2013"

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
        self.blekko_api = blekko.Blekko(source='my_api_key') # Trzeba uzupełnić
        
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
        results_sorted = self.sort_results(res_blekko, res_duck)
        
        return results_sorted
        
        
    def sort_results(self, resultsA, resultsB):
        """ Sortuje wyniki w odpowiedni sposób. """
        
        results = []
        
        """ Liczba list z wynikami / argumentów metody. """
        num_of_lists = 2
        
        indexA = 0
        indexB = 0
        
        for i in range(max((len(resultsA), len(resultsB)))):
            if num_of_lists % (i + 1) and indexA < len(resultsA):
                results.append(resultsA[indexA])
                indexA = indexA + 1
            elif num_of_lists % (i + 2) and indexB < len(resultsB):
                results.append(resultsB[indexB])
                indexB = indexB + 1
        
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
            print >>sys.stderr, str(exc)
            return None
        
        return results