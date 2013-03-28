#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 27, 2013"

# """ Dla funkcji 'sleep' """
# import time

import urllib2
import requests

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
        self.bing_key = 'ffCq52T+iRuKYD5P6rgbQDwDivKj6H0bBSqlmecl4AA='
        
    def get_results(self, list_of_queries):
        """
        Pobiera z wyszukiwarek linki stanowiące odpowiedź za zapytania.
        """
        
        
        for i in range(len(list_of_queries)):
            query = list_of_queries[i]
            query_string = "".join(query)
            
            results_blekko = self.get_results_blekko(query_string)
            #list_of_lists_of_results.append(results_blekko)
            
            #results_duck = self.get_results_duckduckgo(query_string)
            #list_of_lists_of_results.append(results_duck)
        
        """ Posortuj wyniki """
        
        return results_blekko
        
        
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
        URL = "https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/Web?Query='%(query)s'&$top=10&$format=json"
        r = requests.get(URL % {'query': urllib2.quote(query)}, auth=('', 'ffCq52T+iRuKYD5P6rgbQDwDivKj6H0bBSqlmecl4AA='))
        
        #print "\nDuckDuckGo result type: %s\n" % r.type 
        for i in r.json()['d']['results']:
            response = Response()
            response.url = str(i['Url'].encode('utf-8'))
            response.url_title = str(i['Title'].encode('utf-8'))
            results.append(response)

        return results
    
    def _dirty_hack_(self):
        return True


lista = [u'czerwony', u'kapturek']
response_gatherer = ResponseGatherer()

resultaty = response_gatherer.get_results(lista)

for result in resultaty:
    print result.url
    print result.url_title