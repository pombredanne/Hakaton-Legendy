# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 203."""

def add_document(simple_index, document, terms):
    """
    tworzy odwrócony indeks. Funkcja powinna dodawać do słownika
    `simple_index.documents` kolejne nazwy dokumentów jako klucze z
    przyporządkowanymi identyfikatorami (pierwszy dodany dokument ma mieć
    identyfikator 0, drugi - 1 itd). Z kolei lista `terms` zawiera listę
    wyrazów (termów) z dokumentu. Wyrazy mogą się powtarzać. Funkcja ma
    także tworzyć indeks `simple_index.inverted_index`, czyli słownik,
    który wyrazom przyporządkowuje listę identyfikatorów (czasami
    wielokrotnie ten sam identyfikator, jeśli wyraz występuje więcej niż
    raz dokumencie).
    """
    docid = len(simple_index.documents)
    
    simple_index.documents[document] = docid
    
    for term in terms:
        if term in simple_index.inverted_index:
            simple_index.inverted_index[term].append(docid)
        else:
            simple_index.inverted_index[term] = [docid]