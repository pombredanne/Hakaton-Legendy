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

class ResponseGathererTest(unittest.TestCase):
    """ Testy do zdobywacza linków """
    
    def testDuckDuckGo(self):
        """ Prosty test dla DuckDuckGo """
        results = asker.get_results_duckduckgo(simple_query_a)
        
        print "\nDuckDuckGo. Query %s. Results: \n" % simple_query_a
        print results
        
        self.failUnless(len(results) > 0)
        

if __name__ == '__main__':
    unittest.main()