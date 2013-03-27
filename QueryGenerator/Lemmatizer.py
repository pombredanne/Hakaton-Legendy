#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os


class Lemmatizer:
    file_name = os.path.abspath('dictionaries/slownik_lemm.txt')
    """Konstruktor"""
    def __init__(self):
        
        self.lems = dict()


    """Znajduje forme podstawową argumentu słowo"""
    def znajdz(self, slowo):
        self.searchfile = codecs.open(self.file_name, 'r', 'utf-8')
        for line in self.searchfile:
            if slowo in line:
                words = line.split()
                tempik = words[0]
                podst = tempik.replace(",", "")
                self.lems[slowo] = podst
                break
        self.searchfile.close()


    def get_lems(self):
        return self.lems

lemmaitzed = []

lemik = Lemmatizer()
lemik.znajdz(" babijami, ")
lemik.znajdz(" ma, ")


print lemik.get_lems()
print u'mie\u0107'.encode('utf-8')
