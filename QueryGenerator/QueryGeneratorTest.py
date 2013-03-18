#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

"""
Testuje działanie generatora zapytań. 
"""

from QueryGenerator import QueryGenerator

class Task206Test(unittest.TestCase):
    """ Testy do generatora zapytań. """
    
    def testToksNoUnicode(self):
        """ Prosty test tokenizacji. BEZ UNICODE. """
        
        legenda = u'Moja babcia ma bardzo dużo lat. Hola!'
        legenda = legenda + u' podaj herbatę mi.'
        
        tokens_ref = [u'Moja', u'babcia', u'ma', u'bardzo',
                      u'dużo', u'lat', u'Hola',
                      u'podaj', u'herbatę', u'mi']
        
        frequencies = {u'mieć': 0.012}
        lemmas = {u'kosmici' : u'kosmita'}
        
        generator = QueryGenerator(frequencies, lemmas)
        
        gen_tokens = generator.toks(legenda)
        
        self.failUnlessEqual(tokens_ref, gen_tokens)
        
    
    def testToksUnicode(self):
        """ Sprawdza tokenizację. """
        legenda = 'Moja babcia ma bardzo dużo lat. Hola! Powiedziała babcia mi.'
       # legenda = legenda.decode('utf-8')
        
        tokens = ['Moja', 'babcia', 'ma', 'bardzo', 
                    'dużo', 'lat', 'Hola', 
                    'Powiedziała', 'babcia', 'mi' ]
      #  for t in tokens:
      #      t = t.decode('utf-8')
        
        frequencies = {u'mieć': 0.012}
        lemmas = {u'kosmici' : u'kosmita'}
        
        generator = QueryGenerator(frequencies, lemmas)
        
        gen_tokens = generator.toks(legenda)
        
        self.failUnlessEqual(tokens, gen_tokens)
        
    
    def testLemmatization(self):
        """ Sprawdza poprawność lematyzacji. """
        
        tokens = [u'Moja', u'babcia', u'ma', u'bardzo', 
                    u'dużo', u'lat', u'Hola', 
                    u'Powiedziała', u'babcia', u'mi' ]
        
        lemmatized_ref = [u'moje', u'babcia', u'mieć', u'bardzo',
                          u'dużo', u'lat', u'hola', u'powiedzieć',
                          u'babcia', u'ja']
        
        frequencies = {
            u'mieć': 0.012}
        lemmas = {u'kosmici' : u'kosmita',
                  u'mi' : u'ja',
                  u'moja' : u'moje',
                  u'ma' : u'mieć',
                  u'powiedziała' : u'powiedzieć'}
        
        generator = QueryGenerator(frequencies, lemmas)
        
        lemmatized_gen = generator.lemmatise(tokens)
        
        self.failUnlessEqual(lemmatized_ref, lemmatized_gen)
        

    def testRareWords(self):
        """ Sprawdza poprawność znajdowania rzadkich słów. """
        
        lemmatized_legend_list = [u'babcia', 
            u'mieć', u'kot', u'śmierć', u'w', u'autostopowicz']
        
        frequencies = {
            u'mieć': 0.012,
            u'kot': 0.0003,
            u'babcia': 0.006,
            u'autostopowicz': 0.00005,
            u'śmierć': 0.00002,
            u'w' : 0.005
            }
        
        lemmas = {u'kosmici' : u'kosmita',
                  u'mi' : u'mi'}
        rares = [u'śmierć', u'autostopowicz', u'kot']
        
        generator = QueryGenerator(frequencies, lemmas)
        
        rares_gen = generator.find_rare_words(lemmatized_legend_list)
        
        self.failUnlessEqual(rares, rares_gen)


if __name__ == '__main__':
    unittest.main()
