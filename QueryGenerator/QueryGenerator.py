#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 23, 2012"

""" Przetwarzanie języka """
import nltk
import re

""" Sortowanie słownika """
import operator

""" Dostęp do katalogów, plików """
import os
from os import listdir
from os.path import isfile, join
import fnmatch

""" Czytanie plików """
import fileinput

""" Do losowego wyciągania elementów ze zbiorów """
import random

""" Frekwencjoner - do wyciągania liczby wystąpień tokenów """
from Frequencer import Frequencer

""" Lematyzator - do wyciągania form podstawowych wyrazów """
from Lemmatizer import Lemmatizer

class QueryGenerator:
    """ Generuje zbiór zapytań na podstawie tekstu legendy. """
    
    def __init__(self):
        """Konstruktor. 
            frequencies to słownik {słowo : liczba} częstości występowania
            słów w języku polskim. 
        """
        self.frequencer = Frequencer()
        self.lemmatizer = Lemmatizer()
            
        self.garbage_words = self.generate_list_of_garbage_words()
        
        self.story_words = self.generate_list_of_story_words()
        
        self.corpus_dir = os.path.abspath('legends')
        
    def lemmatise(self, legend_toks_list):
        """ Sprowadza tekst legendy do postaci zlematyzowanej. 
            legend_toks_list to lista tokenów legendy. """
        
        #lems_dict = self.lemmatizer.get_lems(legend_toks_list)
        lems_dict = self.lemmatizer
        lemmatized = []
        
        for token in legend_toks_list:
            tok_low = token.lower()
            lems_dict.znajdz(tok_low)

            '''
            if lems_dict.has_key(tok_low):
                lemmatized.append(lems_dict[tok_low])
            else:
                lemmatized.append(tok_low)
            '''
        #lemmatized = lems_dict.get_lems() 
        #return lemmatized 
        return lems_dict.get_lems()
    

    def strip_garbage(self, lemmatized_legend_test):
        """ Usuwa z listy słów zlematyzowanych, słowa-śmieci, np. 'haha',
        'hehe', 'historia', 'prawdziwa', czyli takie, które pojawiają
        się w co drugiej legendzie. """
        
        return [ word for word in lemmatized_legend_test
                if not word in self.garbage_words]
    
    def toks(self, legend):
        """ Tokenizuje tekst legendy. """
        # tokens = nltk.word_tokenize(legend)
        pattern = r'''(?x)
             ([A-Z]\.)+
           | \w+    
           | \w+(-\w+)*        
           | \$?\d+(\.\d+)?%?  
           | [][.,;"'?():-_`]'''
        # return nltk.regexp_tokenize(legend, p3)
        
        p2 = r'(?x)\w+'
        
        p3 = r'\w+'
        
        re_word = re.compile(r'(\w+)', re.UNICODE)
        
        words = []
        
        for word in re.findall(re_word, legend):
            words.append(word.lower())
            
        return words
    
    def random_words(self, set_of_words, number_of_elements):
        """ Wyciąga number_of_elements elementów z set_of_words. """
        
        num = number_of_elements
        if number_of_elements > len(set_of_words):
            num = len(set_of_words)
        
        return random.sample(set_of_words, num)    
    
    
    def generate_queries(self, legend):
        """ Generuje zbiór list będących zapytaniami do wyszukiwarek. """
        
        """ Podstawowy preprocessing """
        # print "\nGenerowanie zapytania..."
        tokens = self.toks(legend)
        # print "\nTokens: "
        # print tokens
        lemmatized_legend_list = self.lemmatise(tokens)
        # print "\nLemmatized: "
        # print lemmatized_legend_list
        garbage_free = self.strip_garbage(lemmatized_legend_list)
        # print "\nGarbage free: "
        # print garbage_free
        
        """ Rzadkie słowa oraz słowa kluczowe """
        rare_words = self.find_rare_words(garbage_free)
        # print "\nRare words: "
        # print rare_words
        keywords = self.keywords(lemmatized_legend_list, rare_words)
        # print "\nKeywords: "
        # print keywords
        
        """ Lista zapytań - list słów """
        queries = []
        
        """ Pierwsza lista to słowa kluczowe """
        query1 = keywords
        queries.append(query1)
        
        """ Kolejne zapytania to kilka losowych elementów ze zbioru
            słów kluczowycy + kilka elementów typowo "legendowych",
            tj. "historia", "koleżanka" - wskazujących na to, że
            mamy do czynienia z historią. """
        
        for i in range(9):
            story_words_num = random.randint(1, 3)
            query = self.random_words(self.story_words, story_words_num)
            keywords_words_num = random.randint(2, 5)
            k_words = self.random_words(keywords, keywords_words_num)
            
            for k in k_words:
                query.append(k)
                
            queries.append(query)
        
        return queries
        
        
    def find_rare_words(self, lemmatized_legend_list):
        """ Wyszukuje rzadkowystępujące (w j. polskim) słowa zawarte
        w liście słów lemmatized_legend_list. 
        Zwraca listę rzadkich słów, w kolejności od najrzadszych. """
        
        """ Uwzględni słowa o częstotliwości mniejszej niż rare_treshold. """
        rare_treshold = 200
        
        """ Znajdzie co najwyzej max_rares rzadkich słów. """
        max_rares = 20
        
        """ Mapowanie słów legendy do częstotliwości występowania w j. pl: """
        freqs = self.frequencer.get_frequencies(lemmatized_legend_list)
                
        # print "\nfreqs: "
        # print freqs
        
        """ Sortowanie słów po częstotliwości ich występowania """
        """ list of tuples sorted by the second element in each tuple. """
        sorted_words = sorted(freqs.iteritems(),
            key=operator.itemgetter(1), reverse=True)
          
        """ Ostateczna lista rzadkich słów """
        rares = []
        
        for key in sorted_words:
            # print "key %s - %d" %(key[0], key[1])
            if key[1] < rare_treshold:
                rares.append(key[0])
            
            if len(rares) >= max_rares:
                break
            
        return rares

    
    def number_of_legends_in_corpus(self):
        """ Liczy legendy w korpusie. """
        
        files = [ f for f in listdir(self.corpus_dir) 
                 if isfile(join(self.corpus_dir, f)) ]
    
        legends_num = 0
    
        prefixes = set()
        
        for f in files:
            chunks = f.split('_');
            if chunks[0] not in prefixes:
                prefixes.add(chunks[0])
                legends_num = legends_num + 1
        
        return legends_num
    
    def keywords(self, lemmatized_legend_text, legend_rare_words):
        """ Generuje zbiór słów kluczowych danej legendy.
        lemmatized_legend_text - lista zlematyzowanych, 
        odśmiecionych (po przebiegu metody strip_garbage) "lemów.
        legend_rare_words - lista rzadkich słów występujących
        w legendzie (stworzona metodą find_rare_words). 
        """
        
        frequency_dist = nltk.FreqDist(lemmatized_legend_text)
        
        # print frequency_dist
        
        return {w for (w, freq) in frequency_dist.items() 
                if freq > 2 and w in legend_rare_words}
        
    def generate_list_of_story_words(self):
        """ Generuje listę słów, które pojawiają się w wielu
        legendach, np. 'historia'. """
        
        story_words = {
           u'historia', u'przyda', u'przydażać', u'przydarzać',
           u'przydarzyła', u'znajomy', u'kumpel', u'historia',
           u'prawdziwy', u'prawda', u'kolega', u'koleżanka',
           u'opowiedzieć'
        }
        
        return story_words 
    
    def generate_list_of_garbage_words(self):
        """ Generuje słowa-śmieci, np. 'haha',
        'hehe', 'historia', 'prawdziwa', czyli takie, które pojawiają
        się w co drugiej legendzie. """
        
        garbage_words = {
            u'haha', u'hehe', u'bardzo', u'dużo',
            u'mieć', u'w', u'hehe', u'prawdziwy',
        }
        
        return garbage_words
