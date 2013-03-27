#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 25, 2012"

import unittest

"""
Testuje działanie zdobywacza linków (z wyszukiwarek)
"""

from ResponseGatherer import ResponseGatherer

asker = ResponseGatherer()

#simple_query_a = 'miejska legenda nerki'
simple_query_a = 'Python'

queries_a = [ ['python', 'programming'], ['python', 'snake'] ]

def print_results_list(results):
    """
    Wypisuje listę wyników (obiektów
    klasy Response z modułu Responses).
    """
    for res in results:
        print "Result. Title: %s, Url: %s, Snippet: %s, Engine %s" \
            %(res.url_title, res.url, res.snippet, res.engine)
        

class ResponseGathererTest(unittest.TestCase):
    """ Testy do zdobywacza linków """
    
    def testDuckDuckGo(self):
        """ Prosty test dla DuckDuckGo """
        results = asker.get_results_duckduckgo(simple_query_a)
        
        print "\nDuckDuckGo. Query %s. Results: \n" % simple_query_a
        print results
        
        self.failUnless(len(results) > 0)
        
    def testWholeSearchA(self):
        """ Testuje całe wyszukiwanie. """
        
        results = asker.get_results(queries_a)
        
        print "\nWhole search query: "
        print queries_a
        print "\nResults: "
        print_results_list(results)
        

if __name__ == '__main__':
    unittest.main()