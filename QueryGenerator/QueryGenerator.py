#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk

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
        
        #return nltk.word_tokenize(legend)
    
    def generate_queries(self, legend, corpus_dir):
        """ Generuje zbiór list będących zapytaniami do wyszukiwarek. """
        tokens = toks(self, legend)
        
        
        
    def find_rare_words(self, lemmatized_text):
        """ Wyszukuje rzadkowystępujące (w j. polskim) słowa zawarte
        w tekście (stringu) lemmatized_text. """
        
        
    def find_keywords(self, rare_words, corpus_dir):
        """ Wyszukuje słowa kluczowe zawarte w rare_keywords, takie, które
        występują w tekstach (plikach) w katalogu corpus_dir. """
    
