#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import codecs

file_name = os.path.abspath('dictionaries/slownik_lemm.txt')
searchfile = codecs.open(file_name, 'r', 'utf-8')

legend = unicode('Kolega raz mi opowiadał jak u niego na wsi łepki po 19 lat dorwali BMW (niewiem z którego roku dokładnie). Okres zimowy, auto zapakowane pięcioma osobnikami w dresach,', "UTF-8")

re_word = re.compile(r'(\w+)', re.UNICODE)
words = []
for word in re.findall(re_word, legend):
	words.append(word.lower())

for i in words:
	print i.encode('utf-8')

words_lem = []
'''
for wordlem in re.search(re_word, self.searchfile):
	words

'''
with open("slownik_lemm.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')