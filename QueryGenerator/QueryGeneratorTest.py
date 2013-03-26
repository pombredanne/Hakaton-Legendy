#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 23, 2012"

import unittest

"""
Testuje działanie generatora zapytań. 
"""

from QueryGenerator import QueryGenerator

generator = QueryGenerator()

class QueryGeneratorTest(unittest.TestCase):
    """ Testy do generatora zapytań. """
    
    def testToksNoUnicode(self):
        """ Prosty test tokenizacji. BEZ UNICODE. """
        
        legenda = u'Moja babcia ma bardzo dużo lat. Hola!'
        legenda = legenda + u' podaj herbatę mi.'
        
        tokens_ref = [u'moja', u'babcia', u'ma', u'bardzo',
                      u'dużo', u'lat', u'hola',
                      u'podaj', u'herbatę', u'mi']
        
        gen_tokens = generator.toks(legenda)
        
        self.failUnlessEqual(tokens_ref, gen_tokens)
        
    
    def testToksUnicode(self):
        """ Sprawdza tokenizację. """
    
        legenda = unicode('Moja babcia ma bardzo dużo lat. ' \
            'Hola! Powiedziała babcia mi.', "UTF-8")
        
        tokens_a = ['moja', 'babcia', 'ma', 'bardzo',
                    'dużo', 'lat', 'hola',
                    'powiedziała', 'babcia', 'mi' ]
        
        tokens = []
        
        for t in tokens_a:
            t = unicode(t, "UTF-8")
            tokens.append(t)
        
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
        
        lemmatized_gen = generator.lemmatise(tokens)
        
        self.failUnlessEqual(lemmatized_ref, lemmatized_gen)
        
        
    def testStripGarbage(self):
        """ Sprawdza poprawność usuwania słów-śmieci. """
        
        lemmatized_legend_list = [u'babcia',
            u'mieć', u'kot', u'śmierć', u'w',
            u'hehe', u'prawdziwy', u'autostopowicz']
        
        legend_garbage_free_ref = [u'babcia',
            u'kot', u'śmierć', u'autostopowicz']
        
        legend_garbage_free_gen = generator.strip_garbage(lemmatized_legend_list)
        
        self.failUnlessEqual(legend_garbage_free_ref, legend_garbage_free_gen)
        

    def testRareWords(self):
        """ Sprawdza poprawność znajdowania rzadkich słów. """
        
        lemmatized_legend_list = [u'babcia', u'olaboga',
            u'mieć', u'kot', u'śmierć', u'w', u'autostopowicz']
        
        rares = [u'autostopowicz', u'olaboga', u'mieć']
        
        rares_gen = generator.find_rare_words(lemmatized_legend_list)
        
        self.failUnlessEqual(rares, rares_gen)
        

    def testLegendsNum(self):
        """ Sprawdza poprawność liczenia liczby legend. """
        
        legends_num_ref = 9
        
        legends_num_gen = generator.number_of_legends_in_corpus()
        
        self.failUnlessEqual(legends_num_ref, legends_num_gen)
        
    
    def testKeywords(self):
        """ Sprawdza poprawność znajdowania słów kluczowych. """
        
        lemmatized_legend_list = [u'babcia',
            u'mieć', u'kot', u'śmierć', u'w', u'autostopowicz',
            u'student', u'narty', u'impreza', u'schody', u'w',
            u'mieć', u'student', u'narty', u'narty', u'student']
        
        rare_words = [u'babcia', u'autostopowicz', u'student',
            u'narty']
        
        keywords_ref = {u'student', u'narty'}
        
        keywords_gen = generator.keywords(lemmatized_legend_list, rare_words)
        
        self.failUnlessEqual(keywords_ref, keywords_gen)
        
        
    def testGenerateQueriesA(self):
        """ Sprawdza 'tylko' poprawność generowania zapytań. """
        
        legenda = unicode('Moja babcia ma bardzo dużo lat. Hola!' \
            ' Student! Podaj herbatę mi, studencie!' \
            ' Wy studenci nic byście nie robili. Zły' \
            ' student, zły! Herbata gdzie jest?! Herbata mówię!', "UTF-8") 
        
        queries = generator.generate_queries(legenda)
        
        self.failUnless(len(queries) > 0)
        
        print "\nGenerated queries: "
        print queries
        

if __name__ == '__main__':
    unittest.main()
