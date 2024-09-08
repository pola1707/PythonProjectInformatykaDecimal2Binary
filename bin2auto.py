number = 137
binarny = []
wynik = 0

while number != 0:
    wynik = 0
    wynik = number % 2
    binarny.append(wynik)
    number = number // 2

binarny.reverse()
print(binarny)