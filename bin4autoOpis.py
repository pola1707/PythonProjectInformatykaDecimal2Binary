def decimal_to_binary(decimal_number): #funkcja do wywołania
    if decimal_number == 0: #sprawdzamy czy liczba to nie zero, jeśli tak to zwracamy 0
        return "0"
    binary_number = "" #lista w której przechowujemy liczbę binarną
    while decimal_number > 0: #dopóki liczba jest większa od zera ta pętla będzie działać
        binary_number = str(decimal_number % 2) + binary_number #zapisanie liczby binarnej
        decimal_number = decimal_number // 2 #zmiejszenie liczby o 2, aby nie utknąć w pętli
    return binary_number #zwrócenie liczby binarnej


decimal_number = 137 #ustalenie liczby
binary_representation = decimal_to_binary(decimal_number) # wywołanie funkcji
print(f"Liczba dziesiętna: {decimal_number} to liczba binarna: {binary_representation}") #oddanie liczby użytkownikowi