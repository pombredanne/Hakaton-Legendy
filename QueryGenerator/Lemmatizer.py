#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 24, 2013"

""" Do wczytania pliku w utf-8 """
import codecs

""" Dostęp do katalogów, plików """
import os

import sys

class Lemmatizer:
    """ Podaje lemy (formy podstawowe) słów """
    
    def __init__(self):
        """ Konstruktor """
        file_name = os.path.abspath('dictionaries/lems.txt')
        self.lems_file = codecs.open(file_name, 'r', 'utf-8')
        self.lems = self.build_dictionary()
        
    def build_dictionary(self):
        """
        Buduje sobie słownik całego pliku :)
        """
        
        lems = dict()
        
        for line in self.lems_file:
            line = line.strip()
            if line == '' or len(line) == 0:
                 break  # koniec pliku
            else:
                parts = line.split(" ")
                word = parts[0]
                lem = parts[1]
                lems[word] = lem
            
        return lems
        
    def get_lems(self, tokens):
        """
        Podaje słownik lemów, tj. słownik {słowo : forma_podstawowa}
        dla podanych tokenów.
        """
            
        lems = dict()
        
        for tt in set(tokens):
            token = tt.lower()
            if token in self.lems:
                lems[token] = self.lems[token]
            else:
                lems[token] = token
        
        return lems
