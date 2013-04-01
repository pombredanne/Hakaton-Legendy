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
                #wynik += "debug-MAX%s" %maxValue
                for k in listaWynikowWyszukiwania:
                    wynik += u"<ul><li><a href=\"%s\">%s</a></li></ul>" %(k, k)
            else:
                listaWynikowWyszukiwania = skrypt.searchIt(maxValue)
                wynik += u"<br /><b>Wyniki wyszukiwania dla:<br /></b><span style=\"color: gray;\"><i>%s</i></span><br />" %tekstLegendy
                #wynik += "debug-MAX%s" %maxValue
                for k in listaWynikowWyszukiwania:
                    wynik += u"<ul><li><a href=\"%s\">%s</a></li></ul>" %(k, k)                
        except ValueError:
            listaWynikowWyszukiwania = skrypt.searchIt(maxValue)
            wynik += u"<br /><b>Wyniki wyszukiwania dla:<br /></b><span style=\"color: gray;\"><i>%s</i></span><br />" %tekstLegendy
            #wynik += "debug-MAX%s" %maxValue
            for k in listaWynikowWyszukiwania:
                wynik += u"<ul><li><a href=\"%s\">%s</a></li></ul>" %(k, k)
        return HttpResponse(wynik)
    return HttpResponse(szablon())
  
    
def szablon():
    html = "<title>Wyszukiwarka legend miejskich</title>"
    html += "<style type=\"text/css\">"
    html += "BODY {font-family: Verdana; background-color: #F7F7F7; margin-left: 200px; margin-right: 200px; margin-bottom: 50px;}"
    html += "a {font-size: 12px;}"
    html += "ul {margin-top: 10px;}"
    html += "</style>"
    html += "<h1>Wyszukiwarka legend miejskich</h1>"
    html += u"<p style=\"font-size: 12px; color: gray;\"><span style=\"color: black\"><b>Zanim skorzystasz!</b><br /></span>Jedną z wykorzystywanych wyszukiwarek jest wyszukiwarka Google, którą można odpytać raz na 10 minut, stąd przy częstszym odpytywaniu zwracane wyniki mogą być niekompletne (czyt. pomniejszone o wyniki Google'a).</p>"
    html += "<FORM ACTION=\"\" METHOD=POST>"
    html += "<TEXTAREA NAME=\"legendyTextArea\" VALUE=\"lTA\" COLS=100 ROWS=5>"
    html += "W tym polu wpisz tekst legendy..."
    html += "</TEXTAREA><br />"
    html += u"<p style=\"font-size: 12px; margin-top: 0px; margin-bottom: 0px;\">Podaj liczbę tokenów lub zostaw puste pole dla domyślnej wartości: <input type=\"text\" name=\"yourV\"></p>"
    html += "<BR />"
    html += "<INPUT TYPE=SUBMIT style=\"font-size: 20px; padding: 5px 100px 5px 100px;\" VALUE=\"Szukaj!\" NAME=\"IUH\" />"
    html += "</FORM>"
    return html
