#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Skrypt import Skrypt
                                          
@csrf_exempt               

def SearchLegend(request):
    szablon()
    skrypt = Skrypt()
    if request.method == 'POST':        
        wynik = szablon()
        tekstLegendy = request.POST['legendyTextArea']
        maxValue = skrypt.tokenise(tekstLegendy)
        yourValue = request.POST['yourV']
        #PRZEKAZYWANIE LICZB SLOW:
        try:
            if int(yourValue)<=int(maxValue):
                listaWynikowWyszukiwania = skrypt.searchIt(yourValue)
                wynik += u"<br /><b>Wyniki wyszukiwania dla:<br /></b><span style=\"color: gray;\"><i>%s</i></span><br />" %tekstLegendy
                wynik += u"<br />"
                wynik += u"Maksymalna liczba tokenów: <b>%s</b>" %maxValue
                wynik += u"<br />"
                wynik += u"Twoja liczba tokenów: <b>%s</b>" %yourValue
                #DWIE LINIJKI PONIZEJ ZMODYFIKOWAC W ZALEZNOSCI CO BEDZIESZ ZWRACAL
                for k in listaWynikowWyszukiwania:
                    wynik += u"<li><a href=\"%s\">%s</a></li>" %(k, k)
            else:
                wynik += u"<br /><b>Wyniki wyszukiwania dla:<br /></b><span style=\"color: gray;\"><i>%s</i></span><br />" %tekstLegendy
                wynik += u"<br />"            
                wynik += u"Maksymalna liczba tokenów: <b>%s</b>" %maxValue
                wynik += u"<br />"
                wynik += u"Twoja liczba tokenów: <b><span style=\"color: red\">%s</span></b>" %yourValue
                wynik += u"<br />"
                wynik += u"<h2>Liczba podanych tokenów nie może przekraczać wartości maksymalnej, która wynosi <b><span style=\"color: red\">%s</span></b> dla bieżącego wyszukiwania. Spróbuj jeszcze raz.</h2>" %maxValue
        #PONIZSZY EXCEPT POWODUJE, ZE JESLI UZYTKOWNIK NIE PODA ZADNEJ LICZBY TOKENOW TO DOMYSLNIE
        #USTALONA ZOSTANIE MOZLIWIE MAKSYMALNA LICZBA TOKENOW
        except ValueError:
            yourValue = maxValue
            listaWynikowWyszukiwania = skrypt.searchIt(yourValue)
            wynik += u"<br /><b>Wyniki wyszukiwania dla:<br /></b><span style=\"color: gray;\"><i>%s</i></span><br />" %tekstLegendy
            wynik += u"<br />"
            wynik += u"Maksymalna liczba tokenów: <b>%s</b>" %maxValue
            wynik += u"<br />"
            wynik += u"Twoja liczba tokenów: <b>%s</b>" %yourValue
            #DWIE LINIJKI PONIZEJ ZMODYFIKOWAC W ZALEZNOSCI CO BEDZIESZ ZWRACAL
            for k in listaWynikowWyszukiwania:
                wynik += u"<li><a href=\"%s\">%s</a></li>" %(k, k)
        return HttpResponse(wynik)
    return HttpResponse(szablon())

def szablon():
    html = "<title>Wyszukiwarka legend miejskich</title>"
    html += "<style type=\"text/css\">"
    html += "BODY {font-family: Verdana; background-color: #F7F7F7; margin-left: 200px; margin-right: 200px;}"
    html += "</style>"
    html += "<h1>Wyszukiwarka legend miejskich</h1>"
    html += u"<p style=\"font-size: 12px; color: gray;\"><span style=\"color: black\"><b>Zanim skorzystasz!</b><br /></span>Jedną z wykorzystywanych wyszukiwarek jest wyszukiwarka Google, którą można odpytać raz na 10 minut, stąd przy częstszym odpytywaniu zwracane wyniki mogą być niekompletne (czyt. pomniejszone o wyniki Google'a).</p>"
    html += "<FORM ACTION=\"\" METHOD=POST>"
    html += "<TEXTAREA NAME=\"legendyTextArea\" VALUE=\"lTA\" COLS=100 ROWS=5>"
    html += "W tym polu wpisz tekst legendy..."
    html += "</TEXTAREA><br />"
    html += u"Podaj liczbę tokenów: <input type=\"text\" name=\"yourV\">"
    html += "<BR />"
    html += "<INPUT TYPE=SUBMIT style=\"font-size: 20px; margin-top: 5px; padding: 5px 100px 5px 100px;\" VALUE=\"Szukaj!\" NAME=\"IUH\" />"
    html += "</FORM>"
    return html      