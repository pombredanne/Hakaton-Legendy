#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 23, 2012"

import unittest

"""
Testuje działanie wyciągacza frekwencji.
"""

from Frequencer import Frequencer

frequencer = Frequencer()    

class FrequencerTest(unittest.TestCase):
    """ Testy do wyciągacza frekwencji """
    

    def testSimpleA(self):
        """ Prosty test """
        tokens = [u"babcia", u"buty", u"a", u"petarda"]
        
        frequencies_ref = {u"babcia": 4212, u"buty": 6621,
                           u"a": 878943, u"petarda": 32}
        
        frequencies_gen = frequencer.get_frequencies(tokens)
        
        print "\nGenerated dict: \n"
        print frequencies_gen
        
        self.failUnless(len(frequencies_ref) == len(frequencies_gen))
        
        self.failUnlessEqual(frequencies_ref, frequencies_gen)
        
    def testSimpleB(self):
        """ Prosty test, drugi """
        
        tokens = [u"wiertło", u"świr", u"ja",
                  u"żandarm", u"ochotnik", u"pierogi",
                  u"trawa", u"ubuntu"]
        
        frequencies_ref = {u"wiertło": 69, u"świr": 159,
                           u"ja": 193249, u"żandarm": 317,
                           u"ochotnik": 134, u"pierogi": 140,
                           u"trawa": 1870, u"ubuntu": 0}
        
        frequencies_gen = frequencer.get_frequencies(tokens)
        
        print "\nGenerated dict: \n"
        print frequencies_gen
        
        self.failUnless(len(frequencies_ref) == len(frequencies_gen))
        
        self.failUnlessEqual(frequencies_ref, frequencies_gen)
    

if __name__ == '__main__':
    unittest.main()
