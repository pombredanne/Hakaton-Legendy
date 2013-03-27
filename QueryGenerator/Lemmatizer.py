#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import re


class Lemmatizer:
    """Konstruktor"""
    def __init__(self):
        file_name = os.path.abspath('dictionaries/slownik_lemm.txt')
        self.searchfile = codecs.open(file_name, 'r', 'utf-8')
        self.lems = dict()


    """Znajduje forme podstawową argumentu słowo"""
    def znajdz(self, slowo):
        for line in self.searchfile:
            if self.findWholeWord(slowo)(line):
                words = line.split()
                tempik = words[0]
                podst = tempik.replace(",", "")
                self.lems[slowo] = podst
                break


    def get_lems(self):
        return self.lems

    def findWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w)).search

'''
lemmaitzed = []

lemik = Lemmatizer()
lemik.znajdz('ma')
lemik.znajdz("babijami")
print lemik.get_lems()
print u'ad\u017cma\u0144ski'.encode('utf-8')

'''