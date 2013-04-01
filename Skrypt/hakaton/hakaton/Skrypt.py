#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib
import re
import requests
import codecs
import urllib2
import simplejson

class Skrypt:

    def __init__(self):
        self.freqs_dict = dict()
        self.words = list()
        self.cleaned_words_list = list()

    def tokenise(self, legend):
        #legend = unicode(raw_legend, 'UTF-8')

        ''' Tworzenie słownika frekwencji słów. W przypadku duplikatów w pliku, leć dalej. '''
        
        with codecs.open('hakaton/frequencies.txt', 'r', 'utf-8') as freq_file:
            for line in freq_file:
                parts = line.split()
                freq_word = parts[0]
                freq_num = int(parts[1])
                if freq_word in self.freqs_dict:
                    continue
                else:
                    self.freqs_dict[freq_word] = freq_num
        freq_file.close()


        '''Rozwalenie tekstu legendy na slowa do listy '''
        re_word = re.compile(r'(\w+)', re.UNICODE)
        for word in re.findall(re_word, legend):
            self.words.append(word.lower())

        ''' Usunięcie tych słów z listy words, których frekwencja przekracza 'maximum' '''

        maximum = 300
        minimum = 70
        
        for i in self.words:
            if i not in self.freqs_dict:
                continue
            elif self.freqs_dict.get(i) > maximum:
                continue
            elif self.freqs_dict.get(i) < maximum and self.freqs_dict.get(i) > minimum:
                self.cleaned_words_list.append(i)
        return len(self.cleaned_words_list)





    def searchIt(self, how_many_words):

        ''' Tworzenie napisu do zapytania, w zaleznosci od argumentu how_many_words '''
        iterator = int(how_many_words)
        query = "legenda miejska ".encode('utf-8') #mały haczyk dodatkowy
        for i in xrange(iterator):
            query = query + self.cleaned_words_list[i].encode('utf-8') + " "
        results = list()

        ''' Implementacja poszczególnych wyszukiwarek '''

        #Bing
        URL = "https://api.datamarket.azure.com/Data.ashx/Bing/SearchWeb/Web?Query='%(query)s'&$top=10&$format=json"
        r = requests.get(URL % {'query': urllib2.quote(query)}, auth=('', 'ffCq52T+iRuKYD5P6rgbQDwDivKj6H0bBSqlmecl4AA='))
        for i in r.json()['d']['results']:
            bing_result_url = str(i['Url'].encode('utf-8'))
            results.append(bing_result_url)

        #DuckDuckGo
        siteDuck = urllib.urlopen("http://duckduckgo.com/html/?q=%s"%query)
        data = siteDuck.read()
        parsed = BeautifulSoup(data)

        extr = 10
        for i in parsed.findAll('div', {'class': re.compile('links_main*')}):
            if extr is 0:
                break
            else:
                extr = extr - 1
                duck_result_url = str(i.a['href'].encode('utf-8'))
                results.append(duck_result_url)

        #Google
        url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s"%urllib.urlencode({'q' : query})
        search_results = urllib.urlopen(url)
        json = simplejson.loads(search_results.read())
        json_results = json['responseData']['results']
        for i in json_results:
            google_url_result = i['url']
            results.append(google_url_result)

        return results
