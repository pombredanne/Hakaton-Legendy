#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 24, 2013"

""" Schemat struktury odpowiedzi """
from Responses import Response

""" Wsparcie dla wyszukiwarki Blekko """
import blekko

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
        res_blekko = get_results_blekko(query1)
        
        
    def get_results_blekko(terms):
        results = []
        try:
            res = self.blekko_api.query(terms)
            for result in res:
                r = Response()
                r.url_title = result.url_title
                r.url = result.url
                r.snippet = result.snippet
                r.engine = "Blekko"
                results.append(r)
                    
        except blekko.BlekkoError as exc:
            print >>sys.stderr, str(exc)
            return None
        return results