#!/usr/bin/python
# -*- coding: utf-8 -*-

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

""" Odwrócony indeks, tf-idf """
from InvertedIndex.SimpleIndex import SimpleIndex
from InvertedIndex.Task201 import add_document
from InvertedIndex.Task206 import cosine_score

class QueryGenerator:
    """ Generuje zbiór zapytań na podstawie tekstu legendy. """
    
    def __init__(self, frequencies, lemmas):
        """Konstruktor. 
            frequencies to słownik {słowo : liczba} częstości występowania
            słów w języku polskim. 
            lemmas to słownik {słowo : słowo_w_postaci_podstawowej}, czyli
            mapowanie ze słów do 'lemów'. """
        self.frequencies = frequencies
        self.lemmas = lemmas
            
        self.garbage_words = self.generate_list_of_garbage_words()
        
        self.story_words = self.generate_list_of_story_words()
        
        self.corpus_dir = os.path.abspath('legends')
        
        self.index = SimpleIndex(dict(), dict())
            
    def lemmatise(self, legend_toks_list):
        """ Sprowadza tekst legendy do postaci zlematyzowanej. 
            legend_toks_list to lista tokenów legendy. """
        
        lemmatized = []
        
        for token in legend_toks_list:
            tok_low = token.lower()
            if self.lemmas.has_key(tok_low):
                lemmatized.append(self.lemmas[tok_low])
            else:
                lemmatized.append(tok_low)
                
        return lemmatized
    
    def strip_garbage(self, lemmatized_legend_test):
        """ Usuwa z listy słów zlematyzowanych, słowa-śmieci, np. 'haha',
        'hehe', 'historia', 'prawdziwa', czyli takie, które pojawiają
        się w co drugiej legendzie. """
        
        return [ word for word in lemmatized_legend_test
                if not word in self.garbage_words]
        
        """
        garbage_free = []
        
        for word in lemmatized_legend_test:
            if word not in self.garbage_words:
                garbage_free.append(word)
                
        return garbage_free
        """
    
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
        
    
    def generate_queries(self, legend):
        """ Generuje zbiór list będących zapytaniami do wyszukiwarek. """
        
        """ Podstawowy preprocessing """
        tokens = toks(self, legend)
        lemmatized_legend_list = self.lemmatise(tokens)
        garbage_free = self.strip_garbage(lemmatized_legend_list)
        
        """ Rzadkie słowa oraz słowa kluczowe """
        rare_words = self.find_rare_words(lemmatized_legend_list)
        keywords = self.keywords(lemmatized_legend_list, rare_words)
        
        
        
        
    def find_rare_words(self, lemmatized_legend_list):
        """ Wyszukuje rzadkowystępujące (w j. polskim) słowa zawarte
        w liście słów lemmatized_legend_list. 
        Zwraca listę rzadkich słów, w kolejności od najrzadszych. """
        
        """ Uwzględni słowa o częstotliwości mniejszej niż rare_treshold. """
        rare_treshold = 0.001
        
        """ Znajdzie co najwyzej max_rares rzadkich słów. """
        max_rares = 12
        
        freqs = dict()
        
        """ Mapowanie słów legendy do częstotliwości występowania w j. pl: """
        for word in lemmatized_legend_list:
            if self.frequencies.has_key(word):
                freqs[word] = self.frequencies[word]
            else:
                freqs[word] = 0.0
        
        """ Sortowanie słów po częstotliwości ich występowania """
        """ list of tuples sorted by the second element in each tuple. """
        sorted_words = sorted(freqs.iteritems(), key=operator.itemgetter(1))
          
        """ Ostateczna lista rzadkich słów """
        rares = []
        
        for key in sorted_words:
            if key[1] < rare_treshold:
                rares.append(key[0])
            
            if len(rares) == max_rares:
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
    
    def generate_list_of_garbage_words(self):
        """ Generuje słowa-śmieci, np. 'haha',
        'hehe', 'historia', 'prawdziwa', czyli takie, które pojawiają
        się w co drugiej legendzie. """
        
        garbage_words = {
            u'haha', u'hehe',
            u'mieć', u'w', u'hehe', u'prawdziwy',
        }
        
        return garbage_words
