#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os

class Lemmatizer:
    """Konstruktor"""
    def __init__(self):
        file_name = os.path.abspath('slownik_lemm.txt')
        self.searchfile = codecs.open(file_name, 'r', 'utf-8')
        self.lems = dict()


    """Znajduje forme podstawową argumentu słowo"""
    def znajdz(self, slowo):
        for line in self.searchfile:
            if slowo in line:
                words = line.split()
                tempik = words[0]
                podst = tempik.replace(",", "")
                self.lems[slowo] = podst
                break
        


    def get_lems(self):
        return self.lems

