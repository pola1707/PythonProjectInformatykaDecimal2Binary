def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number


decimal_number = int(input())
binary_representation = decimal_to_binary(decimal_number)
print(f"Liczba dziesiętna: {decimal_number} to liczba binarna: {binary_representation}")