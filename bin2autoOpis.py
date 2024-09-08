number = 137 #ustalenie liczby
binarny = [] #stworzenie listy gdzie zapisujemy liczbę binarną
wynik = 0 #zmienna zapamiętująca wynik działania

while number != 0: #pętla działająca do póki liczba dziesietna nie będzie 0 (koniec działania)
    wynik = 0 #resetowanie wyniku
    wynik = number % 2 #rozbijanie na części pierwsze
    binarny.append(wynik) #dodawanie wyniku do liczby binarnej (0/1)
    number = number // 2 #dzielenie liczby na 2

binarny.reverse() #odwrócenie binarnej (tył to teraz przód, przód to tył)(zapisuje się na odwrót)
print(binarny) #oddanie liczby w binarnym użytkownikowi
