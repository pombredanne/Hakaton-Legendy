#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Bartosz Kosowski"
__date__ = "$March 23, 2012"

class Response:
    """
    Odpowiedź - jeden element.
    Elementy:
        url_title - tytuł
        url - adres url
        snippet - fragment
        engine - wyszukiwarka
    """
    
    def __init__(self):
        """ Konstruktor """
        self.url_title = ""
        self.url = ""
        self.snippet - ""
        self.engine = ""