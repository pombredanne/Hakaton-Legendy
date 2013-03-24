#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 23, 2012"

""" Do wczytania pliku w utf-8 """
import codecs

""" Dostęp do katalogów, plików """
import os

import sys

class Frequencer:
    """ Podaje częstości wystąpień słów """
    
    def __init__(self):
        """ Konstruktor """
        file_name = os.path.abspath('dictionaries/frequencies2.txt')
        self.frequencies_file = codecs.open(file_name, 'r', 'utf-8')
        self.frequencies = self.build_dictionary()
        
    def build_dictionary(self):
        """
        Buduje sobie słownik całego pliku :)
        """
        
        freqs = dict()
        
        for line in self.frequencies_file:
            line = line.strip()
            if line == '' or len(line) == 0:
                 break  # koniec pliku
            else:
                parts = line.split(" ")
                word = parts[0]
                
                try:
                    num = int(parts[1])
                    freqs[word] = num
                except ValueError:
                    sys.stderr.write("Frequencer error: empty line. Moving on...\n")
            
        return freqs
        
    def get_frequencies(self, tokens):
        """
        Podaje słownik frekwencji dla tokenów.
        """
            
        freqs = dict()
        
        for token in set(tokens):
            if token in self.frequencies:
                freqs[token] = self.frequencies[token]
            else:
                freqs[token] = 0
        
        return freqs
