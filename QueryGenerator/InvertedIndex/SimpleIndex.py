# -*- coding: utf-8 -*-
"""Materiały do zadań na II ćwiczenia."""

import shelve
import re
import math
from BeautifulSoup import BeautifulSoup

class SimpleIndex:
    """Prosty odwrócony indeks"""
    def __init__(self, index_dict, doc_dict):
        """Konstruktor"""
        self.inverted_index = index_dict
        self.documents = doc_dict

    def __del__(self):
        """Destruktor"""
        pass

    def process(self, url, content):
        """Dodaje dokument do indeksu"""
        if(url not in self.documents):
            terms = self.extract_terms(content)
            if len(terms):
                add_document(self, url, terms)
        else:
            print "Document '%s' already indexed, skipping" % url

    def extract_terms(self, document):
        """Zwraca wyrazy zawarte na stronie."""
        words = []
        re_word = re.compile(r'(\w+)', re.UNICODE)
        soup = BeautifulSoup(document)
        texts = soup.findAll(text=True)
        for text in texts:
            if text.parent.name in ['style', 'script',
                                    '[document]', 'head', 'title']:
                continue
            if re.match('<!--.*-->', text):
                continue

            for word in re.findall(re_word, text):
                words.append(word.lower().encode("utf-8"))
        return words

    def query(self, querystring, score, topn=10):
        """Odpytuje indeks podaną metodą oceny"""

        query = querystring.lower().split()
        scores = [(document, score(query, document))
                   for document in self.documents]

        return sorted(scores, key=lambda x:-x[1])[0:topn]

    ###########################################################################

if __name__ == '__main__':
    INDEX_SHELF = shelve.open("index.inv", writeback=True);
    DOC_SHELF = shelve.open("index.did", writeback=True);

    MYINDEX = SimpleIndex(INDEX_SHELF, DOC_SHELF)

    RESULTS = MYINDEX.query("inteligentne systemy informacyjne",
                            cosine_score, 10)

    for page, page_score in RESULTS:
        print page_score, "-", page

    INDEX_SHELF.close()
    DOC_SHELF.close()
