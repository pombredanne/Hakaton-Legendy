#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 24, 2013"

import unittest

"""
Testuje działanie lematyzatora
"""

from Lemmatizer import Lemmatizer

lemmatizer = Lemmatizer()    

class LemmatizerTest(unittest.TestCase):
    """ Testy do wyciągacza lemów """
    
    def testLemsA(self):
        """ Łatwy test. """
        
        tokens = [u'moja', u'babcia', u'ma', u'bardzo',
                    u'dużo', u'lat', u'hola',
                    u'powiedziała', u'babcia', u'mi' ]
        
        lemmatized_ref = set([u'moje', u'babcia', u'mieć', u'bardzo',
                          u'dużo', u'lat', u'hola', u'powiedzieć',
                          u'babcia', u'ja'])
        
        lemmatized_gen_dict = lemmatizer.get_lems(tokens)
        
        lemmatized_gen = set()
        
        for word, lem in lemmatized_gen_dict.items():
            lemmatized_gen.add(lem)
        
        #print "\Original set:"
        #print lemmatized_ref
        #print "\Generated set:"
        #print lemmatized_gen
        
        self.failUnlessEqual(lemmatized_ref, lemmatized_gen)


if __name__ == '__main__':
    unittest.main()
