#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import codecs
from pprint import pprint

def tokenizuj(legend):
    
    file_name = os.path.abspath('slownik_lemm.txt')

    '''Ładowanie słownika lemów do listy, by szybciej działało '''
    data = []
    with codecs.open('slownik_lemm.txt', 'r', 'utf-8') as myfile:
        for line in myfile:
            data.append(line.rstrip())
    myfile.close()

    ''' Tworzenie słownika frekwencji słów. W przypadku duplikatów w pliku, leć dalej. '''
    freqs_dict = dict()
    with codecs.open('frequencies.txt', 'r', 'utf-8') as freq_file:
        for line in freq_file:
            line1 = line.strip()
            parts = line.split()
            freq_word = parts[0]
            freq_num = int(parts[1])
            if freq_word in freqs_dict:
                continue
            else:
                freqs_dict[freq_word] = freq_num
    freq_file.close()


    '''Rozwalenie tekstu legendy na slowa do listy '''
    re_word = re.compile(r'(\w+)', re.UNICODE)
    words = []
    for word in re.findall(re_word, legend):
        words.append(word.lower())

    #for i in words:
    #    print i.encode('utf-8')
    #pprint(freqs_dict)
    #print freqs_dict.get('nic')

    ''' Usunięcie tych słów z listy words, których frekwencja przekracza 'maximum' '''

    maximum = 300
    minimum = 70

    cleaned_words_list = []

    for i in words:
        if i not in freqs_dict:
            continue
        elif freqs_dict.get(i) > maximum:
            continue
        elif freqs_dict.get(i) < maximum and freqs_dict.get(i) > minimum:
            cleaned_words_list.append(i)
    #pprint(words)

    for i in cleaned_words_list:
        print i.encode('utf-8')



    '''


    #Lematyzowanie zmiennej slowo w liście data

    words_lem = []
    for _word in words:
        re_lemik = re.compile(r'\b%s\b'%_word, re.UNICODE)
        for line in data:
            if re_lemik.search(line):
                lematyzowane = line.split()
                words_lem.append(lematyzowane[0])
                break

    for i in words_lem:
        print i.encode('utf-8')
    '''

    #print words_lem[0].encode('utf-8')
    #print data[0].encode('utf-8')


legend = unicode('tutaj będzie tekst legendy', "UTF-8")