#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Krzysztof Wisznarewski"
__date__ = "$March 28, 2012"

class Response:
    """
    Odpowiedź - jeden element.
    Elementy:
        url_title - tytuł
        url - adres url
    """
    
    def __init__(self):
        """ Konstruktor """
        self.url_title = ""
        self.url = ""