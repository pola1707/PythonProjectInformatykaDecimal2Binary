decimal_number = int(input()) #ustalenie liczby

binary_number = "" #lista przechowująca liczbę binarną

if decimal_number == 0: #sprawdzenie czy liczba dziesiętna wynosi 0, jak tak to oddanie 0
    binary_number = "0"
else:
    while decimal_number > 0: #pętla trawjąca do póki liczba nie będzie >=0
        binary_number = str(decimal_number % 2) + binary_number #dodanie liczby do binarnej (1/0)
        decimal_number = decimal_number // 2 #podzielenie liczby na 2 aby nie utknąć w pętli

print(f"Liczba binarna: {binary_number}") #oddanie liczby binarnej użytkownikowi