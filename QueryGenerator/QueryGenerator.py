#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Przetwarzanie języka """
import nltk

""" Sortowanie słownika """
import operator


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
        
        garbage_free = []
        
        for word in lemmatized_legend_test:
            if word not in self.garbage_words:
                garbage_free.append(word)
                
        return garbage_free
        
    
    def toks(selfs, legend):
        """ Tokenizuje tekst legendy. """
        # tokens = nltk.word_tokenize(legend)
        pattern = r'''(?x)
             ([A-Z]\.)+
           | \w+    
           | \w+(-\w+)*        
           | \$?\d+(\.\d+)?%?  
           | [][.,;"'?():-_`]'''
        
        p2 = r'(?x)\w+'
        
        p3 = r'\w+'
        
        return nltk.regexp_tokenize(legend, p3)
        
        # return nltk.word_tokenize(legend)
    
    def generate_queries(self, legend, corpus_dir):
        """ Generuje zbiór list będących zapytaniami do wyszukiwarek. """
        tokens = toks(self, legend)
        
        
        
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
        
    def find_keywords(self, rare_words, corpus_dir):
        """ Wyszukuje słowa kluczowe zawarte w rare_keywords, takie, które
        występują w tekstach (plikach) w katalogu corpus_dir. """
    
    def generate_list_of_garbage_words(self):
        """ Generuje słowa-śmieci, np. 'haha',
        'hehe', 'historia', 'prawdziwa', czyli takie, które pojawiają
        się w co drugiej legendzie. """
        
        garbage_words = {
        u'haha', u'hehe', u'prawdziwy', u'prawda', u'kolega', u'koleżanka',
        u'znajomy', u'przydażać', u'przydarzać', u'przydarzyła', u'kumpel',
        u'historia', u'mieć', u'w', u'hehe', u'prawdziwy',
        }
        
        return garbage_words
