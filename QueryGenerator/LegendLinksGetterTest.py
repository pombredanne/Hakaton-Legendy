#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 25, 2012"

import unittest

""" Do wczytania pliku w utf-8 """
import codecs

""" Dostęp do katalogów, plików """
import os

import sys

from LegendLinksGetter import LegendLinksGetter

"""
Testuje działanie sklejki generatora zapytań
z pobieraczem linków.
"""

links_getter = LegendLinksGetter()

class LegendLinksGetterTest(unittest.TestCase):
    """ Testy do sklejki """
    
    def testToksNoUnicode(self):
        """ Prosty test """
        
        legend = readLegend('na_akF.txt')
        
        results = links_getter.search(legend)
        
        self.failUnless(len(results) > 0)

def readLegend(fileName):
    """
    Wczytuje legendę z pliku.
    """
    
    f = os.path.abspath('legends/' + fileName)
    file = codecs.open(f, 'r', 'utf-8')
    
    legend = ''
    for line in file:
        legend = legend + line + ' '
    
    return legend      
  

if __name__ == '__main__':
    unittest.main()
